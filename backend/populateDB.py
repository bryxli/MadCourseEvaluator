import requests
import json
import mysql.connector
import madgrades as mg # Custom MadGrades Script for Grade Distributions
import praw            # PRAW: Python Reddit API Wrapper
from praw.models import MoreComments
from RMP.ratemyprof_api import RateMyProfApi # Public & Modified RMP API for Professor Data
import config
import time

# Documentation Reference: README Subsection 1.1

# Establish connection to MySQL DB
conn = mysql.connector.connect(
   user = config.user,
   password = config.password, 
   host = config.host,
   database = config.database
)

# Instantiate an instance of PRAW's Reddit object
reddit = praw.Reddit(client_id = config.PRAW_client_id, 
                    client_secret = config.PRAW_client_secret, 
                    username = config.r_username, 
                    password = config.r_password,
                    user_agent = config.PRAW_user_agent)

# Instantiate PRAW Subreddit Object for r/UWMadison
uwmadison_subreddit = reddit.subreddit('UWMadison')
reddit_url = 'https://www.reddit.com'

# (DOCS: 1.1.1.1)
def PopCourses(testing = False):
    """
    Function to populate the courses table with all courses at UW-Madison. Entries contain a cUID, the course's name, 
    the course's subject, the course's code, the course's credits, and the course's description.

    Data: Course data scraped from guide.wisc.edu with fetchAll.py script, preloaded in comp_sci_test_courses.json.
    """
    if testing:
        # Start a timer to measure the time it takes to populate the professors table
        start = time.time()
        print("----------PopCourses-----------")

    file = open('./major_test_sample/major_courses.json', 'r') # Open the JSON file containing test CS courses
    data = json.load(file)          # Load the JSON file into a dictionary
    cursor = conn.cursor()          # Create a cursor object to execute SQL queries

    # For each course, try inserting its course data into the DB
    for key in data.keys():
        cName = data[key]['name']
        cSubject =  data[key]['subject']
        cCode = data[key]['code']
        cCredits = data[key]['credits']
        cDescription = data[key]['description'] 
        cReq = data[key]['requisite']

        try:
            cursor.execute("INSERT INTO courses (cName, cSubject, cCode, cCredits, cDescription, cReq) VALUES (%s, %s, %s, %s, %s, %s)", (cName, cSubject, cCode, cCredits, cDescription, cReq,))
            conn.commit()
        except Exception as e: # cr:
            print(e)
            #print("Error inserting course into database")
            
    cursor.close()
    if testing:
        print("PopCourses Runtime: ", time.time() - start, " seconds.")
    pass

# (DOCS: 1.1.1.2)
def PopProfessors(testing = False):
    """
    Function to populate the professors table with all professors at UW-Madison. Iterates over the two RMP school UIDs and calls the helper function to populate the table.
    Entries contain a pUID, the professor's first name, last name, and pData (where pData is a dictionary of all RateMyProfessor data).

    Data: Professor data scraped from RateMyProfessorss.com.
    """
    if testing:
        # Start a timer to measure the time it takes to populate the professors table
        start = time.time()
        print("----------PopProfessors-----------")

    file = open('all-professors.json', 'r') # Open the JSON file containing professors
    data = json.load(file)          # Load the JSON file into a dictionary
    cursor = conn.cursor()          # Create a cursor object to execute SQL queries

    # For each course, try inserting its course data into the DB
    for key in data:
        prof_json = data[key]
        pData = json.dumps(prof_json)  # Convert the JSON professor data to JSON formatted string

        try:
            # Check if the professor is already in the DB
            cursor.execute("SELECT * FROM professors WHERE pName = %s", (prof_json['name'],))
            result = cursor.fetchall()
            
            # If the professor is not in the DB, insert the professor into the DB
            if len(result) == 0:
                # Insert course into the database's professors table
                cursor.execute("INSERT INTO professors (pName, pData) VALUES (%s, %s)", (prof_json['name'], pData))
                conn.commit()

        except Exception as e:
            print(e)
            # print("Error inserting professor into database")

            
    cursor.close()
    if testing:
        print("PopProfessors: ", time.time() - start, " seconds.")
    pass


# (DOCS: 1.1.1.3)
def PopRedditComments(testing = False):
    """
    Function to populate the rc (reddit comments) table with all comments that are relevant to a certain course that were posted to r/UWMadison. 
    
    Data: Comment data scraped from r/UWMadison using PRAW.
    """
    if testing:
        # Start a timer to measure the time it takes to populate the professors table
        start = time.time()
        print("-------PopRedditComments-------")

    cursor = conn.cursor() 
    cursor.execute("SELECT cUID, cName, cCode, cSubject FROM courses") # Get the cUID, and cCode of all courses

    courses = cursor.fetchall() # Store all course datac

    # Create a course acronym (DOCS: 1.1.2.4)
    for course in courses:
        if(course[3] == 'Statistics' or course[3] == 'Mathematics' or course[3] == 'Computer Sciences'): #only choose selective majors now
            cNum = ''.join(filter(str.isdigit, course[2]))  # Extract all numeric characters from the course's code
            search = course[2]
            # Extract the first letter of all alphabetical characters in the course's code
            acronym = ''
            for word in course[2].split():
                if word[0].isalpha():
                    acronym += word[0]
                        
            # Keyword analysis using full course code, or the courses acronym + course number (e.g. CS506 or CS 506)
            for submission in uwmadison_subreddit.search(search, limit=50):
                if (search.lower() in submission.title.lower()) or (acronym + cNum in submission.title) or (acronym + ' ' + cNum in submission.title): 
                    # A CommentForest is a list of top-level comments each of which contains a CommentForest of replies.
                    # Submission.comments attribute's comment forest (since each replacement requires a network request)
                    try:
                    # Iterate through each top-level comment in the comment forest
                        for comment in submission.comments.list():
                            if ((25 < len(comment.body) < 1000) and ((comment.score > 2) or (cNum in comment.body))):
                                
                                    # Insert reddit comment into the database's rc table
                                    cursor.execute("INSERT INTO rc (cUID, comBody, comLink, comVotes) VALUES (%s, %s, %s, %s)", (course[0], comment.body, reddit_url+comment.permalink, comment.score,))
                                    conn.commit()
                    except Exception as e: # cr:
                        print(e)
        else:
            continue
    
    cursor.close()
    if testing:
        print("PopRedditComments Runtime: ", time.time() - start, " seconds.")
    pass

def PopTeaches(testing = False):
    """
    Function to populate the teaches table with cUIDs and pUIDs for each course. Defining what courses each professor teaches.
    
    Data: Professor data scraped from MadGrades per course.
    """
    if testing:
        # Start a timer to measure the time it takes to populate the professors table
        start = time.time()
        print("----------PopTeaches----------")

    cursor = conn.cursor() 
    cursor.execute("SELECT cUID, cCode FROM courses") # Get the cUID, and cCode of all courses
    courses = cursor.fetchall() 

    # For each course in the courses table, find the professor(s) that teach the course
    for course in courses:
        cUID = course[0]
        cCode = course[1]
        grade_distributions = mg.MadGrades(cCode) # Get the grade distribution for the course from MadGrades.com
        
        course_professors = [] # List of professors that teach the course
        all_term_data = []     # List of all term data for the course

        # Make sure MadGrades returns a dictionary of grade distribution data for each course
        if(grade_distributions is None):
            break

        # Get the section data for each term
        for i in range(len(grade_distributions["courseOfferings"])):
            single_term_data = grade_distributions["courseOfferings"][i]["sections"]
            all_term_data.append(single_term_data) # Store all term data into a list

        num_terms = len(all_term_data) 

        # For every term, get the professor's name and add it to the list of professors for that course
        for j in range(num_terms):
            for k in range(len(all_term_data[j])):

                # If the course has multiple professors, add each professor to the list of professors for that course
                if(len(all_term_data[j][k]["instructors"]) > 1):
                    for L in range(len(all_term_data[j][k]["instructors"])):
                        if all_term_data[j][k]["instructors"][L] not in course_professors:
                            course_professors.append(all_term_data[j][k]["instructors"][L])

                # If the course has only one professor, add that professor to the list of professors for that course if they aren't already in the list
                else:
                    if all_term_data[j][k]["instructors"][0] not in course_professors:
                        course_professors.append(all_term_data[j][k]["instructors"][0])

        # For every professor that teaches a course, get their pUID and insert it into the teaches table for that course
        for professor in course_professors: 
            try:
                prof_name = professor['name'] 
                prof_name = prof_name.replace("X / ", "").replace("S / ", "") # Solution to a bug in the MadGrades API (depricated?)

                # Get the pUID of the professor
                cursor.execute("SELECT pUID from professors where pName Like %s", (prof_name,))
                pUID = cursor.fetchone()

                # If the professor is in the professors table, add them to the teaches table with the course's cUID
                if pUID is not None:
                    try:
                        cursor.execute("INSERT INTO teaches (cUID, pUID) VALUES (%s, %s)", (cUID, pUID[0],)) 
                        conn.commit()
                    except Exception as e:
                        print(e)
            except Exception as e:
                print(e)
                # print("Error inserting into teaches table")
                # if testing and pUID is None:
                # print("Professor not found in professors table: ", prof_name)
        
    cursor.close()
    if testing:
        print("PopTeaches Runtime: ", time.time() - start, " seconds.")
    pass

def PopDB(testing = False):
    """
    Function that populated the entire database by calling all Pop Functions.
    """
    if testing:
        start = time.time()
        print("-------------PopDB-------------")
        print("Populating Database...")

    # PopCourses(testing)
    # PopProfessors(testing)
    # PopRedditComments(testing)
    PopTeaches(testing)

    if testing:
        print("Database Populated.")
        print("PopDB Runtime: ", time.time() - start, " seconds.")
        print("-------------------------------")
    pass

if __name__ == '__main__': 
    PopDB(testing = True) # Run all Pop Functions
    # PopDB(testing = False) # Run all Pop Functions