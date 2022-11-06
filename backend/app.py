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



@app.route('/course/<cName>', methods=['GET','POST'])
def coursePage(cName):
    """
    """
    return "Test"

@app.route('/professor/<pUID>', methods=['GET','POST'])
def professorPage(pUID):
    """
    """
    search = pUID # TODO
    pass


if __name__ == '__main__':
    app.run(debug=True, port = 5000)