from flask import Flask, render_template, request, flash, redirect, url_for, session
import requests
import mysql.connector
from datetime import datetime, tzinfo
import json
import config # Move to gitignore
import madgrades as mg


app = Flask(__name__)
app.secret_key = config.secret

# Config DB
app.config['MYSQL_HOST'] = 'host'
app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = 'pw'
app.config['MYSQL_DB'] = 'db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


# Establish connection to the database
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

    ex. Course Data => cUID, cName, cSubject, cCode, cCredits, cDescription, cReq
    """
    cursor = conn.cursor() # Create a cursor object to execute SQL queries

    cursor.execute("SELECT * FROM courses") # Execute SQL query

    # Fetch all the rows from the database as json
    all_courses = cursor.fetchall()

    i = 0
    all_course_json_data = {}
    for course in all_courses:
        course_json_data = {'cUID': None, 'cName': None, 'cSubject': None, 'cCode': None, 'cCredits': None, 'cDescription': None, 'cReq': None}
        if i == 5:
            break
        course_json_data['cUID'] = course[0]
        course_json_data['cName'] = course[1]
        course_json_data['cSubject'] = course[2]
        course_json_data['cCode'] = course[3]
        course_json_data['cCredits'] = course[4]
        course_json_data['cDescription'] = course[5]
        course_json_data['cReq'] = course[6]
        all_course_json_data[course_json_data['cUID']] = course_json_data
        i+=1

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
        if i == 3:
            break
        pUID = prof[0]
        pData = json.loads(prof[1])
        all_profs_json_data[pUID] = pData
        i+=1
        
    cursor.close()   
    return all_profs_json_data



@app.route('/course/<cUID>', methods=['GET','POST'])
def coursePage(cUID):
    """
    Specific Course endpoint: returns all data associated with a specific course page.
    Data per course -> 1. All course information from courses table.
                       2. A list of all professors who have taught the course recently.
                       3. A list of all Reddit comments associated with the course.
                       4. Grade distribution for the course.
    """
    
    cursor = conn.cursor() # Create a cursor object to execute SQL queries
    full_course_data_json = {}

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

    # Store course data in the full course data json that will be returned
    full_course_data_json['course_data'] = course_json_data

    # 2. Get all professors who have taught the course recently
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

    # Store all professors who have taught the course recently in the full course data json that will be returned
    full_course_data_json['professors'] = all_prof_json_data

    # 3. Get all Reddit comments associated with the course
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

    # Store all Reddit comments associated with the course in the full course data json that will be returned
    full_course_data_json['reddit_comments'] = all_rc_json_data

    # 4. Get grade distribution for the course
    grade_distribution = mg.MadGrades(course_json_data['cCode']) # Get grade distribution for the course using the course code

    full_course_data_json['grade_distribution'] = grade_distribution


    return full_course_data_json

@app.route('/professor/<pUID>', methods=['GET','POST'])
def professorPage(pUID):
    """
    """
    search = pUID # TODO
    pass


if __name__ == '__main__':
    app.run(debug=True, port = 5000)