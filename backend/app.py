from flask import Flask, render_template, request, flash, redirect, url_for, session
import requests
from flask_mysqldb import MySQL
from datetime import datetime, tzinfo
import json
import config # Move to gitignore


app = Flask(__name__)
app.secret_key = config.secret

# Config DB
app.config['MYSQL_HOST'] = 'host'
app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = 'pw'
app.config['MYSQL_DB'] = 'db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# init MYSQL
mysql = MySQL(app)

# ~~ CONSTANTS ~~
# 1. MadGrades
madGrades_course_url = 'https://api.madgrades.com/v1/courses/'
madGrades_query_url = madGrades_course_url +'?query='
madgrades_api_token = config.madgrades_api_token                # Instantiate Madgrades API Token
auth_header = {'Authorization': 'Token ' + madgrades_api_token} # Authorization header, required for API call


@app.route('/', methods=['GET','POST'])
def index():
    """ 
    """
    return "Test" 

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

# TODO: Error handling
def MadGrades(courseName):
    """
    Pulls grade distributions from every course at UW-Madison and populates the grade-distributions table
    """
    search = courseName
    response = requests.get(madGrades_query_url + search, headers=auth_header) # API call to access list of courses matching search query
    course_listings = response.json()                                                  
    course_url = course_listings['results'][0]['url']                          # Get API Endpoint URL of first course in list
    response = requests.get(course_url, headers=auth_header)                   # API call to get course data associated with select course
    full_course_data = response.json()                                  
    grades_url = full_course_data['gradesUrl']                                 # Get API Endpoint URL of grade distribution data                                            
    response = requests.get(grades_url, headers=auth_header)                   # API call to access grade distribution data
    courses = response.json()                                                  # Course offerings dictionary, with a list of dictionaries for each 
    return(courses)

if __name__ == '__main__':
    app.run(debug=True, port = 5000)