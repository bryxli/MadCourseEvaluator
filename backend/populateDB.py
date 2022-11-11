# Needed Python Libraries
import requests
import json
import mysql.connector
# Custom MadGrades Script for Grade Distributions
import madgrades as mg
# PRAW: Python Reddit API Wrapper
import praw
from praw.models import MoreComments
# Public & Modified RMP API for Professor Data
from RMP.ratemyprof_api import RateMyProfApi
# Application Configuration (Private) Information
import config

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

# Instantiate UW-Madison RateMyProfessor Object (DOCS: 1.1.2.1)
uwm_rmp_sid_1 = "1256"  # RMP School ID #1
uwm_rmp_sid_2 = "18418" # RMP School ID #2

api_1 = RateMyProfApi(uwm_rmp_sid_1, testing = True) # (DOCS: 1.1.2.2)
api_2 = RateMyProfApi(uwm_rmp_sid_2, testing = True)

reddit_url = 'https://www.reddit.com'

# TODO: PopCourses() is finished!
# (DOCS: 1.1.1.1)
def PopCourses():
    """
    Function to populate the courses table with all courses at UW-Madison.
    Entries contain a cUID, the course's name, the course's subject, the course's code, the course's credits, and the course's description.
    """

    file = open('./compsci_test_sample/list_courses.json', 'r') # Open the JSON file containing all UW-Madison courses (pre-scraped)
    data = json.load(file)          # Load the JSON file into a dictionary
    cursor = conn.cursor()          # Create a cursor object to execute SQL queries

    # For each course at UW-Madison, try inserting its course data into the DB
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
        except Exception as e:
            print(e)
            #print("Error inserting course into database")
            
    cursor.close()
    pass

def PopProfessorsHelper(professor_data):
    """
    Helper function to populate the professors table with all professors at UW-Madison.

    """
    cursor = conn.cursor() 

    # Iterating through every UW professor on RMP, and store the information in a String
    for professor in professor_data:
        prof_json = {}                                          
        professor = professor_data[professor]                               
        prof_json['name'] = professor.first_name + " " + professor.last_name 
        prof_json['dept'] = professor.department              
        prof_json['RMPID'] = professor.ratemyprof_id          
        prof_json['RMPRating'] = professor.overall_rating        
        prof_json['RMPTotalRatings'] = professor.num_of_ratings 
        prof_json['RMPRatingClass'] = professor.rating_class
        pData = json.dumps(prof_json)  # Convert the JSON object to a string

        try:
            # Insert course into the database's professors table
            cursor.execute("INSERT INTO professors (pName, pData) VALUES (%s, %s)", (prof_json['name'], pData))
            conn.commit()
        except Exception as e:
            print(e)
            # print("Error inserting professor into database")
      
    cursor.close()
    pass

# TODO: PopProfessors() is finished!
# (DOCS: 1.1.1.2)
def PopProfessors():
    """
    Function to populate the professors table with all professors at UW-Madison. Iterates over the two RMP school IDs and calls the helper function to populate the table.
    Entries contain a pUID, the professor's first name, last name, and pData (where pData is a dictionary of all RateMyProfessor data).

    Sample pData : {'Fname': 'Peter', 'Lname': 'Adamczyk', 'dept': 'Mechanical Engineering', 'RMPID': 2215832, 'RMPRating': 4.9, 'RMPTotalRatings': 12, 'RMPRatingClass': 'good'}
    """
    professors_data = []

    professors_data.append(api_1.scrape_professors()) # (DOCS: 1.1.2.3)
    professors_data.append(api_2.scrape_professors())

    for data in professors_data:
        PopProfessorsHelper(data)
    pass

 # TODO: PopRedditComments() is finished.
# (DOCS: 1.1.1.3)
def PopRedditComments():
    """
    Function to populate the rc (reddit comments) table with all comments that are relevant to a certain course that were posted to r/UWMadison. 
    Entries contain a comment ID, the comment's text, a link to the comment, the comment's upvotes, and the cUID of the course the comment is about.
    """
    cursor = conn.cursor() 

    file = open('./compsci_test_sample/list_courses.json', 'r') # Open the JSON file containing all UW-Madison courses (pre-scraped)
    data = json.load(file)                  # Load the JSON file into a dictionary
    cursor = conn.cursor(buffered=True) 
    for key in data.keys():
        courseCode = data[key]['code'] 
        cursor.execute("SELECT cUID, cName, cCode FROM courses WHERE cCode Like %s", (courseCode,)) # Get the cUID, and cCode of all courses

        courses = cursor.fetchall() # Store all course datac

        # TODO: FIGURE OUT WHAT SEARCHES TO DO

        # Create a course acronym (DOCS: 1.1.2.4)
        for course in courses:
            cNum = ''.join(filter(str.isdigit, course[2]))  # Extract all numeric characters from the course's code
            search = course[2]
            # Extract the first letter of all alphabetical characters in the course's code
            acronym = ''
            for word in course[2].split():
                if word[0].isalpha():
                    acronym += word[0]

            # print(acronym)
            # print(search)
            # search = cNum

            # Searching for posts that have either the full course code, or the courses acronym + course number (e.g. CS506 or CS 506)
            for submission in uwmadison_subreddit.search(search, limit=50):
                if (search.lower() in submission.title.lower()) or (acronym + cNum in submission.title) or (acronym + ' ' + cNum in submission.title): 
                    # print(submission.title) # Print the submission's title
                    submission.comments.replace_more(limit=10) # Return only the top three comments from the comment tree
                    for comment in submission.comments.list():
                        if ((comment.score > 2) and (25 < len(comment.body) < 1000)) or (cNum in comment.body):
                            try:
                                # Insert reddit comment into the database's rc table
                                cursor.execute("INSERT INTO rc (cUID, comBody, comLink, comVotes) VALUES (%s, %s, %s, %s)", (course[0], comment.body, reddit_url+comment.permalink, comment.score,))
                                conn.commit()
                            except Exception as e:
                                print(e)
                                print("Error inserting reddit comment into database")
    cursor.close()
    pass

# TODO: PopTeaches() is finished.
def PopTeaches():
    """
    Function to populate the teaches table with cUIDs and pUIDs for each course. Defining what courses each professor teaches.
    Entries contain a cUID and a pUID.
    """
    file = open('./compsci_test_sample/list_courses.json', 'r') # Open the JSON file containing all UW-Madison courses (pre-scraped)
    data = json.load(file)                  # Load the JSON file into a dictionary
    cursor = conn.cursor(buffered=True) 
    for key in data.keys():
        courseCode = data[key]['code'] 
        cursor.execute("SELECT cUID, cCode FROM courses WHERE cCode Like %s", (courseCode,)) # Get the cUID, and cCode of all courses

        courses = cursor.fetchall() 
        for course in courses:
  
            cUID = course[0]
            cCode = course[1]
            search = cCode
            grade_distributions = mg.MadGrades(search)
            course_professors = []
            all_term_data = []

            # If the course has no grade distribution, we won't find any professors for that course
            if(grade_distributions is None):
                break

            # Get every single semester's data for a course
            for i in range(len(grade_distributions["courseOfferings"])):
                single_term_data = grade_distributions["courseOfferings"][i]["sections"]
                all_term_data.append(single_term_data)

            num_terms = len(all_term_data) 
            # For every semester, get the professor's name and add it to the list of professors for that course
            for j in range(num_terms):
                for k in range(len(all_term_data[j])):
                    # If the course has multiple professors, add each professor to the list of professors for that course
                    if(len(all_term_data[j][k]["instructors"]) > 1):
                        for L in range(len(all_term_data[j][k]["instructors"])):
                                #print(all_term_data[j][k]["instructors"][L])
                            if all_term_data[j][k]["instructors"][L] not in course_professors:
                                course_professors.append(all_term_data[j][k]["instructors"][L])
                    # If the course has only one professor, add that professor to the list of professors for that course if they aren't already in the list
                    else:
                        if all_term_data[j][k]["instructors"][0] not in course_professors:
                            course_professors.append(all_term_data[j][k]["instructors"][0])

            # For every professor that teaches a course, get their pUID and insert it into the teaches table for that course
            for professor in course_professors:
                prof_name = professor['name'] 
                cursor.execute("SELECT pUID from professors where pName Like %s", (prof_name,))
                pUID = cursor.fetchone()
                if pUID is not None:
                    try:
                        cursor.execute("INSERT INTO teaches (cUID, pUID) VALUES (%s, %s)", (cUID, pUID[0],))
                        conn.commit()
                    except Exception as e:
                        print(e)
                        print("Error inserting into teaches table")
                else:
                    print("Professor not found")
                    print(prof_name)

    cursor.close()
    pass


def PopDB():
    """
    Function that populated the entire database by calling all Pop Functions.
    """
    # PopCourses()
    # PopProfessors()
    # PopRedditComments()
    PopTeaches()
    return

if __name__ == '__main__':
    PopDB() # Run all Pop Functions
