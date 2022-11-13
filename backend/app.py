# Needed Python Libraries
import requests
import json
import mysql.connector
# Flask Imports
from flask import Flask, render_template, request, flash, redirect, url_for, session
# Custom MadGrades Script for Grade Distributions
import madgrades as mg
# Application Configuration (Private) Information
import config


app = Flask(__name__)
app.secret_key = config.secret 

# Config DB
# app.config['MYSQL_HOST'] = 'host'
# app.config['MYSQL_USER'] = 'user'
# app.config['MYSQL_PASSWORD'] = 'pw'
# app.config['MYSQL_DB'] = 'db'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Establish connection to the DB
conn = mysql.connector.connect(
   user = config.user,
   password = config.password, 
   host = config.host,
   database = config.database
)

@app.route('/all-courses', methods=['GET','POST'])
def AllCourses():
    """
    All Courses endpoint: Returns JSON of all courses at the university along with all fields associated with each course.
    """
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM courses") # Store all data on all courses
    all_courses = cursor.fetchall()

    i = 0
    all_course_json_data = {}
    for course in all_courses:
        course_json_data = {'cUID': None, 'cName': None, 'cCode': None}
        course_json_data['cUID'] = course[0]
        course_json_data['cName'] = course[1]
        course_json_data['cCode'] = course[3] 
        all_course_json_data[course_json_data['cUID']] = course_json_data

    cursor.close()
    return all_course_json_data

@app.route('/all-profs', methods=['GET','POST'])
def AllProfs():
    """
    All Professors endpoint: returns a list of all courses at the university along with all fields associated with each course.

    ex. Professors Data => pUID, pName, pData
    """
    cursor = conn.cursor() # Create a cursor object to execute SQL queries

    cursor.execute("SELECT pUID, pData FROM professors") # Execute SQL query

    # Fetch all the rows from professors table
    all_profs = cursor.fetchall()

    i = 0
    all_profs_json_data = {}
    for prof in all_profs:
        pUID = prof[0]
        pData = json.loads(prof[1])
        all_profs_json_data[pUID] = pData

        
    cursor.close()   
    return all_profs_json_data


@app.route('/course-info/<cUID>', methods=['GET','POST'])
def courseInfo(cUID):
    """
    Returns all course information from courses table.
    """
    cursor = conn.cursor() # Create a cursor object to execute SQL queries

    # 1. Get course data from courses table, 
    cursor.execute("SELECT * FROM courses WHERE cUID = %s", (cUID,)) # Execute SQL query

    # Fetch all the course data from the database
    course_data = cursor.fetchall()[0]  

    course_json_data = {'cUID': None, 'cName': None, 'cSubject': None, 'cCode': None, 'cCredits': None, 'cDescription': None, 'cReq': None} # Create a dictionary to store course data

    # Store course data in dictionary
    course_json_data['cUID'] = course_data[0]
    course_json_data['cName'] = course_data[1]
    course_json_data['cSubject'] = course_data[2]
    course_json_data['cCode'] = course_data[3]
    course_json_data['cCredits'] = course_data[4]
    course_json_data['cDescription'] = course_data[5]
    course_json_data['cReq'] = course_data[6]

    cursor.close()
    return course_json_data

@app.route('/course-profs/<cUID>', methods=['GET','POST'])
def courseProfs(cUID):
    """
    Returns all professors who have taught the course recently.
    """
    cursor = conn.cursor() # Create a cursor object to execute SQL queries

    # Get all the professors who have taught the course recently
    cursor.execute("SELECT pUID, pData FROM professors WHERE pUID IN (SELECT pUID FROM teaches WHERE cUID = %s)", (cUID,)) # Execute SQL query

    # Fetch all the rows from professors table
    all_profs = cursor.fetchall() 
    all_prof_json_data = {} # Create a dictionary mapping pUID to pData

    # Populate the all_prof_json_data dictionary
    for prof in all_profs:
        pUID = prof[0]
        pData = json.loads(prof[1])
        all_prof_json_data[pUID] = pData

    cursor.close()
    return all_prof_json_data

@app.route('/reddit-comments/<cUID>', methods=['GET','POST'])
def redditComments(cUID):
    """
    Returns all Reddit comments associated with the course.
    """
    cursor = conn.cursor() # Create a cursor object to execute SQL queries
    
    # Get all Reddit comments associated with the course
    cursor.execute("SELECT * FROM rc WHERE cUID = %s", (cUID,)) # Execute SQL query

    # Fetch all the rows from rc table
    all_rc = cursor.fetchall()

    all_rc_json_data = {} # Create a dictionary mapping rcUID to rcData

    # Populate the all_rc_json_data dictionary
    for rc in all_rc:
        comID = rc[0]
        comBody = rc[1]
        comLink = rc[2]
        comVotes = rc[3]
        all_rc_json_data[comID] = {'comBody': comBody, 'comLink': comLink, 'comVotes': comVotes}

    return all_rc_json_data


@app.route('/grade-distribution/<cUID>', methods=['GET','POST'])
def gradeDistribution(cUID):
    """
    Returns grade distributions for the course.
    """
    cursor = conn.cursor() # Create a cursor object to execute SQL queries
    cursor.execute("SELECT cCode FROM courses WHERE cUID = %s", (cUID,))
    cCode = cursor.fetchall()[0][0]
    grade_distribution = mg.MadGrades(cCode) # Get grade distribution for the course using the course code
    return grade_distribution

@app.route('/professor/<pUID>', methods=['GET','POST'])
def professorPage(pUID):
    """
    Specific Professor endpoint: returns all data associated with a specific professor page.
    Data per Professor -> 1. All professor information from professors table.
                          2. List of courses taught by the professor.
    """
    cursor = conn.cursor() # Create a cursor object to execute SQL queries
    search = pUID
    full_professor_data_json = {}
    all_course_json_data = {}

    # 1. Get professor data from professors table,
    cursor.execute("SELECT pData FROM professors WHERE pUID = %s", (search,)) # Execute SQL query

    # Fetch all the professor data from the database
    prof_data = cursor.fetchall()[0][0]

    # Store professor data in the full professor data json that will be returned
    full_professor_data_json['professor_data'] = json.loads(prof_data)

    # 2. Get all courses taught by the professor
    cursor.execute("SELECT cUID, cName, cSubject, cCode, cCredits, cDescription, cReq FROM courses WHERE cUID IN (SELECT cUID FROM teaches WHERE pUID = %s)", (search,)) # Execute SQL query

    # Fetch all the rows from courses table
    all_courses = cursor.fetchall()

    for course in all_courses:
        course_json_data = {'cUID': None, 'cName': None, 'cSubject': None, 'cCode': None, 'cCredits': None, 'cDescription': None, 'cReq': None} # Create a dictionary to store course data
        # Store course data in dictionary
        course_json_data['cUID'] = course[0]
        course_json_data['cName'] = course[1]
        course_json_data['cSubject'] = course[2]
        course_json_data['cCode'] = course[3]
        course_json_data['cCredits'] = course[4]
        course_json_data['cDescription'] = course[5]
        course_json_data['cReq'] = course[6]
        all_course_json_data[course_json_data['cUID']] = course_json_data

    # Store all courses taught by the professor in the full professor data json that will be returned
    full_professor_data_json['courses-taught'] = all_course_json_data

    return full_professor_data_json


if __name__ == '__main__':
    app.run(debug=True, port = 5000)