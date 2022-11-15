import requests
import json
import mysql.connector
from flask import Flask, render_template, request, flash, redirect, url_for, session # Flask Imports
import madgrades as mg # Custom MadGrades Script for Grade Distributions
import config # Application Configuration (Private) Information
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

db_uri =  'mysql://' + config.user + ':' + config.password + '@' + config.host + '/' + config.database
db = SQLAlchemy()

app = Flask(__name__)
app.secret_key = config.secret
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
engine = create_engine(db_uri)                 

############################################################
# TODO: Models.py script, need to initialize MySQL database 
db.init_app(app) # Initialize the Database
with app.app_context(): # Create the Database Tables from models.py
    db.create_all()     # Create the Database
############################################################

@app.route('/all-courses', methods=['GET','POST'])
def AllCourses():
    """
    All Courses endpoint: Returns JSON of all courses at the university along with all fields associated with each course.
    """
    connection = engine.raw_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM courses") # Store all data on all courses
    all_courses = cursor.fetchall()
    all_course_json_data = {}
    for course in all_courses:
        course_json_data = {'cUID': None, 'cName': None, 'cCode': None}
        course_json_data['cUID'] = course[0]
        course_json_data['cName'] = course[1]
        course_json_data['cCode'] = course[3] 
        all_course_json_data[course_json_data['cUID']] = course_json_data

    cursor.close()
    connection.close()
    return all_course_json_data

@app.route('/all-profs', methods=['GET','POST'])
def AllProfs():
    """
    All Professors endpoint: returns a list of all courses at the university along with all fields associated with each course.

    ex. Professors Data => pUID, pName, pData
    """
    connection = engine.raw_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT pUID, pData FROM professors") # Execute SQL query
    all_profs = cursor.fetchall()  # Fetch all the rows from professors table
    all_profs_json_data = {}
    for prof in all_profs:
        pUID = prof[0]
        pData = json.loads(prof[1])
        all_profs_json_data[pUID] = pData
    cursor.close()
    connection.close() 
    return all_profs_json_data


@app.route('/course-info/<cUID>', methods=['GET','POST'])
def courseInfo(cUID):
    """
    Returns all course information from courses table.
    """
    connection = engine.raw_connection()
    cursor = connection.cursor()
    
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
    connection.close() 
    return course_json_data

@app.route('/course-profs/<cUID>', methods=['GET','POST'])
def courseProfs(cUID):
    """
    Returns all professors who have taught the course recently.
    """
    connection = engine.raw_connection()
    cursor = connection.cursor()
    
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
    connection.close()
    return all_prof_json_data

@app.route('/reddit-comments/<cUID>', methods=['GET','POST'])
def redditComments(cUID):
    """
    Returns all Reddit comments associated with the course.
    """
    connection = engine.raw_connection()
    cursor = connection.cursor()
    
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

    cursor.close()
    connection.close()
    return all_rc_json_data


@app.route('/grade-distribution/<cUID>', methods=['GET','POST'])
def gradeDistribution(cUID):
    """
    Returns grade distributions for the course.
    """
    connection = engine.raw_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT cCode FROM courses WHERE cUID = %s", (cUID,))
    cCode = cursor.fetchall()[0][0]
    grade_distribution = mg.MadGrades(cCode) # Get grade distribution for the course using the course code
    return grade_distribution


@app.route('/prof-info/<pUID>', methods=['GET','POST'])
def professorInfo(pUID):
    """
    Specific Professor Info endpoint: returns all RateMyProfessor data for a professor
    associated with the given pUID.
    """
    connection = engine.raw_connection()
    cursor = connection.cursor()
    search = pUID
    professor_data_json = {}

    # Get professor data from professors table,
    cursor.execute("SELECT pData FROM professors WHERE pUID = %s", (search,)) # Execute SQL query
    prof_data = cursor.fetchall()[0][0] # Fetch all the professor data from the database
    professor_data_json['professor_data'] = json.loads(prof_data) # Store professor data in the full professor data json that will be returned

    cursor.close()
    connection.close()
    return professor_data_json

@app.route('/prof-courses/<pUID>', methods=['GET','POST'])
def professorCourses(pUID):
    """
    Professor's Courses endpoint: returns all courses taught by a professor associated with the given pUID.
    """
    connection = engine.raw_connection()
    cursor = connection.cursor()
    search = pUID
    course_data_json = {}

    # Get the course ID data from teaches table,
    cursor.execute("SELECT cUID FROM teaches WHERE pUID = %s", (search,)) # Execute SQL query
    list_courseID = cursor.fetchall()

    for courseID in list_courseID:
        courseID = courseID[0]
        cursor.execute("SELECT cName, cSubject, cCode, cCredits, cDescription, cReq FROM courses WHERE cUID = %s", (courseID,))
        course_data = cursor.fetchall()
        course_json_data = {'cName': None, 'cSubject': None, 'cCode': None, 'cCredits': None, 'cDescription': None, 'cReq': None} 
        
        # Store course data in dictionary
        course_data = course_data[0]
        course_json_data['cName'] = course_data[0]
        course_json_data['cSubject'] = course_data[1]
        course_json_data['cCode'] = course_data[2]
        course_json_data['cCredits'] = course_data[3]
        course_json_data['cDescription'] = course_data[4]
        course_json_data['cReq'] = course_data[5]
        course_data_json[courseID] = course_json_data

    cursor.close()
    connection.close()
    return course_data_json

if __name__ == '__main__':
    app.run(debug=True, port = 5000)