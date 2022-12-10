"""
Flask application for MadCourseEvaluator back end web API.
"""
__author__ = "Peter Bryant, Jarvis Jia"

import json
import mysql.connector
from flask import Flask
import madgrades as mg # Custom MadGrades Script for Grade Distributions
import config          # Application Configuration (Private) Information
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_cors import CORS, cross_origin


db_uri =  'mysql://' + config.user + ':' + config.password + '@' + config.host + '/' + config.database
db = SQLAlchemy()

app = Flask(__name__) 
CORS(app) # Enable CORS for all routes
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = config.secret 
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri  # Set SQLAlchemy URI
engine = create_engine(db_uri)                  # Create SQLAlchemy Engine

@app.route('/all-courses', methods=['GET','POST'])
def AllCourses():
    """
    All Courses endpoint: Returns JSON of all courses at the university along with all fields associated with each course.
    """
    conn = engine.raw_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses") # Store all data on all courses

    if cursor.rowcount == 0: # If no rows are returned, return an empty dictionary with key 'error'
        return {'error': 'No courses found for route /all-courses.'}

    all_courses = cursor.fetchall()
    all_course_json_data = {}

    # For each course, store all course data in a dictionary
    for course in all_courses:
        course_json_data = {'cUID': None, 'cName': None, 'cCode': None}
        course_json_data['cUID'] = course[0]
        course_json_data['cName'] = course[1] 
        course_json_data['cCode'] = course[3] 
        all_course_json_data[course_json_data['cUID']] = course_json_data

    cursor.close() 
    conn.close()   
    return all_course_json_data

@app.route('/all-profs', methods=['GET','POST'])
def AllProfs():
    """
    All Professors endpoint: returns a dictionary of all professors at the university along with all fields associated with each professor.
    """
    conn = engine.raw_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT pUID, pData FROM professors") # Execute SQL query

    if cursor.rowcount == 0: # If no rows are returned, return an empty dictionary with key 'error'
        return {'error': 'No professors found for route /all-profs.'}

    all_profs = cursor.fetchall()  # Fetch all the rows from professors table
    all_profs_json_data = {}

    # Stor all professor data in a dictionary
    for prof in all_profs:
        pUID = prof[0]
        pData = json.loads(prof[1])
        all_profs_json_data[pUID] = pData

    cursor.close()
    conn.close()
    return all_profs_json_data

@app.route('/course-info/<cUID>', methods=['GET','POST'])
def courseInfo(cUID):
    """
    Returns all course information from courses table.
    """
    conn = engine.raw_connection()
    cursor = conn.cursor()
    
    # Get the corresponding course data from courses table:
    cursor.execute("SELECT * FROM courses WHERE cUID = %s", (cUID,))   # Execute SQL query

    if cursor.rowcount == 0: # If no rows are returned, return an empty dictionary with key 'error'
        return {'error': 'No professors found for route /course-info/' + cUID + '.'}

    course_data = cursor.fetchall()[0]                                 # Fetch all the course data for the given cUID
    course_json_data = {'cUID': None, 'cName': None, 'cSubject': None, # Create a dictionary to store course data
                        'cCode': None, 'cCredits': None, 'cDescription': None, 'cReq': None} 
    
    # Populate the course dictionary
    course_json_data['cUID'] = course_data[0]
    course_json_data['cName'] = course_data[1]
    course_json_data['cSubject'] = course_data[2]
    course_json_data['cCode'] = course_data[3]
    course_json_data['cCredits'] = course_data[4]
    course_json_data['cDescription'] = course_data[5]
    course_json_data['cReq'] = course_data[6]

    cursor.close()
    conn.close() 
    return course_json_data

@app.route('/course-profs/<cUID>', methods=['GET','POST'])
def courseProfs(cUID):
    """
    Returns all professors who have taught the course recently.
    """
    conn = engine.raw_connection()
    cursor = conn.cursor()
    
    q = "SELECT pUID, pData FROM professors WHERE pUID IN (SELECT pUID FROM teaches WHERE cUID = %s)"
    cursor.execute(q, (cUID,)) # Get all the professors who have taught the course recently

    if cursor.rowcount == 0: # If no rows are returned, return an empty dictionary with key 'error'
        return {'error': 'No professors found for route /course-profs/' + cUID + '.'}

    all_profs = cursor.fetchall() # Fetch all the rows from professors table

    all_prof_json_data = {} # Create a dictionary mapping pUID to pData

    # Populate the all_prof_json_data dictionary
    for prof in all_profs:
        pUID = prof[0]
        pData = json.loads(prof[1])
        all_prof_json_data[pUID] = pData

    cursor.close()
    conn.close()
    return all_prof_json_data

@app.route('/reddit-comments/<cUID>', methods=['GET','POST'])
def redditComments(cUID):
    """
    Returns all Reddit comments associated with the course.
    """
    conn = engine.raw_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM rc WHERE cUID = %s", (cUID,)) # Get all Reddit comments associated with the course

    if cursor.rowcount == 0: # If no rows are returned, return an empty dictionary with key 'error'
        return {'error': 'No professors found for route /reddit-comments/' + cUID + '.'}

    all_rc = cursor.fetchall()  # Fetch all the rows from rc table

    all_rc_json_data = {} # Create a dictionary mapping rcUID to rcData

    # Populate the all_rc_json_data dictionary with all Reddit comment data
    for rc in all_rc:
        comID = rc[0]
        comBody = rc[1]
        comLink = rc[2]
        comVotes = rc[3]
        all_rc_json_data[comID] = {'comBody': comBody, 'comLink': comLink, 'comVotes': comVotes}

    cursor.close()
    conn.close()
    return all_rc_json_data

@app.route('/grade-distribution/<cUID>', methods=['GET','POST'])
def gradeDistribution(cUID):
    """
    Returns grade distributions for the provided course.
    """
    conn = engine.raw_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT cCode FROM courses WHERE cUID = %s", (cUID,)) # Get the course code for the course
    cCode= cursor.fetchall()[0][0] # Fetch the course code and strip the whitespace

    if cursor.rowcount == 0: # If no rows are returned, return an empty dictionary with key 'error'
        return {'error': 'No courses found for route /grade-distribution/' + cUID + '.'}
  
    grade_distribution = mg.MadGrades(cCode) # Get grade distribution for the course using the course code

    # Get the cumulative grade distribution for each professor
    grade_distribution['professor_cumulative_grade_distribution'] = {}

    # Get the name of all professors who have taught the course in the database
    cursor.execute("SELECT p.pUID, p.pName from professors p, courses c, teaches t WHERE c.cCode = %s and c.cUID = t.cUID and p.pUID = t.pUID", (cCode,))

    if cursor.rowcount == 0: # If no rows are returned, return an empty dictionary with key 'error'
        return {'error': 'No professors found for route /grade-distribution/' + cUID + '.'}

    course_profs = cursor.fetchall() # Fetch all the professor names for professors who have taught the course

    # For each professor, populate the grade_distribution dictionary with their cumulative grade distribution (sum over all sections)
    for prof_info in course_profs:
        prof_pUID = prof_info[0]
        prof_name = prof_info[1]
        grade_distribution['professor_cumulative_grade_distribution'][prof_pUID] = {}
        grade_distribution['professor_cumulative_grade_distribution'][prof_pUID]['name'] = prof_name
        grade_distribution['professor_cumulative_grade_distribution'][prof_pUID]['aCount'] = 0
        grade_distribution['professor_cumulative_grade_distribution'][prof_pUID]['abCount'] = 0
        grade_distribution['professor_cumulative_grade_distribution'][prof_pUID]['bCount'] = 0
        grade_distribution['professor_cumulative_grade_distribution'][prof_pUID]['bcCount'] = 0 
        grade_distribution['professor_cumulative_grade_distribution'][prof_pUID]['cCount'] = 0
        grade_distribution['professor_cumulative_grade_distribution'][prof_pUID]['crCount'] = 0
        grade_distribution['professor_cumulative_grade_distribution'][prof_pUID]['dCount'] = 0
        grade_distribution['professor_cumulative_grade_distribution'][prof_pUID]['fCount'] = 0
        grade_distribution['professor_cumulative_grade_distribution'][prof_pUID]['iCount'] = 0
        grade_distribution['professor_cumulative_grade_distribution'][prof_pUID]['nCount'] = 0
        grade_distribution['professor_cumulative_grade_distribution'][prof_pUID]['nrCount'] = 0
        grade_distribution['professor_cumulative_grade_distribution'][prof_pUID]['nwCount'] = 0
        grade_distribution['professor_cumulative_grade_distribution'][prof_pUID]['otherCount'] = 0
        grade_distribution['professor_cumulative_grade_distribution'][prof_pUID]['pCount'] = 0
        grade_distribution['professor_cumulative_grade_distribution'][prof_pUID]['sCount'] = 0
        grade_distribution['professor_cumulative_grade_distribution'][prof_pUID]['total'] = 0
        grade_distribution['professor_cumulative_grade_distribution'][prof_pUID]['uCount'] = 0

        # For each grade distribution, add the grade counts to the cumulative grade distribution for the professor
        for key in grade_distribution['professor_cumulative_grade_distribution'][prof_pUID].keys() - {'name'}:
            for i in range(len(grade_distribution["courseOfferings"])):
                for j in range(len(range(len(grade_distribution["courseOfferings"][i]['sections'])))):
                    for k in range(len(grade_distribution["courseOfferings"][i]['sections'][j]['instructors'])):
                        API_prof_name = grade_distribution["courseOfferings"][i]['sections'][j]['instructors'][k]['name']
                        # If the professor name in the API contains "X / ", remove the "X / " from the name
                        if "X / " in API_prof_name:
                            API_prof_name = API_prof_name.split("X / ")[1]
                        # If the professor name is in the returned API data, add the grade counts to the cumulative grade distribution for the professor
                        if API_prof_name== prof_name.upper():
                            grade_distribution['professor_cumulative_grade_distribution'][prof_pUID][key] += grade_distribution["courseOfferings"][i]['sections'][j][key]
    cursor.close()
    conn.close()
    return grade_distribution

@app.route('/prof-info/<pUID>', methods=['GET','POST'])
def professorInfo(pUID):
    """
    Specific Professor Info endpoint: returns all RateMyProfessor data for a professor
    associated with the given pUID.
    """
    conn = engine.raw_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT pData FROM professors WHERE pUID = %s", (pUID,)) # Get professor data from professors table

    if cursor.rowcount == 0: # If no rows are returned, return an empty dictionary with key 'error'
        return {'error': 'No professors found for route /prof-info/' + pUID + '.'}

    prof_data = cursor.fetchall()[0][0]    # Fetch all the professor data
    professor_data = json.loads(prof_data) # Store professor data in the full professor data json that will be returned

    cursor.close()
    conn.close()
    return professor_data

@app.route('/prof-courses/<pUID>', methods=['GET','POST'])
def professorCourses(pUID):
    """
    Returns all courses taught by a professor associated with the given pUID.
    """
    conn= engine.raw_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT cUID FROM teaches WHERE pUID = %s", (pUID,)) # Get the course ID data from teaches table
    list_courseID = cursor.fetchall()

    if cursor.rowcount == 0: # If no rows are returned, return an empty dictionary with key 'error'
        return {'error': 'No courses found for route /prof-courses/' + pUID + '.'}

    full_course_data_json = {}

    # For each course, get the course data from the courses table
    for courseID in list_courseID:
        courseID = str(courseID[0])
        cursor.execute("SELECT cName, cSubject, cCode, cCredits, cDescription, cReq FROM courses WHERE cUID = %s", (courseID,)) 
        course_data = cursor.fetchall()

        # Store course data in dictionary
        course_json_data = {'cName': None, 'cSubject': None, 'cCode': None, 'cCredits': None, 'cDescription': None, 'cReq': None} 
        course_data = course_data[0]
        course_json_data['cName'] = course_data[0]
        course_json_data['cSubject'] = course_data[1]
        course_json_data['cCode'] = course_data[2]
        course_json_data['cCredits'] = course_data[3]
        course_json_data['cDescription'] = course_data[4]
        course_json_data['cReq'] = course_data[5]

        # If a course already exists in the dictionary wtih the same 'cName', do not add it to the dictionary
        unique_course = True
        for key in full_course_data_json.keys():
            if course_json_data['cName'] == full_course_data_json[key]['cName']:
                unique_course = False
                break
        if unique_course:
            full_course_data_json[courseID] = course_json_data

    cursor.close()
    conn.close()
    return full_course_data_json

if __name__ == '__main__':
    app.run(debug=True, port = 5000)