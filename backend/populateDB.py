import requests
import config
import praw
from praw.models import MoreComments
from RMP.ratemyprof_api import RateMyProfApi
import json
import mysql.connector

# Establish connection to the database
conn = mysql.connector.connect(
    user = config.user,
    password = config.password, 
    host = config.host,
    database = config.database
)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Instantiate an instance of PRAW's Reddit class
reddit = praw.Reddit(client_id = config.PRAW_client_id, 
                    client_secret = config.PRAW_client_secret,
                    username = config.r_username, 
                    password = config.r_password,
                    user_agent = config.PRAW_user_agent)

# Instantiate PRAW Subreddit Object
uwmadison_subreddit = reddit.subreddit('UWMadison')

# Instantiate Madgrades API Token
madgrades_api_token = config.madgrades_api_token
auth_header = {'Authorization': 'Token ' + madgrades_api_token} # Authorization header, required for API call

# Instantiate UW-Madison RateMyProfesso Object
uwm_rmp_sid = "1256" # RMP School ID
api = RateMyProfApi(uwm_rmp_sid, testing = True)

# URL Constants
madGrades_course_url = 'https://api.madgrades.com/v1/courses/'
madGrades_query_url = madGrades_course_url +'?query='
reddit_url = 'https://www.reddit.com'


"""
Script to automate populating the MYSQL database
"""

def PopCourses():
    """
    Function to populate the courses table with all courses at UW-Madison.
    Entries contain a cUID, the course's name, the course's subject, the course's code, the course's credits, and the course's description.
    """

    file = open('fake.json', 'r') # Open the JSON file containing all UW-Madison courses, TODO replace with the full list of courses

    data = json.load(file) # Load the JSON file into a dictionary

    cursor = conn.cursor() # Create a cursor object to execute SQL queries

    # For each course in the dictionary, get all the courses fields and insert into the table
    for key in data.keys():
        cName = data[key]['name']
        # cSubject =  data[key]['subject']
        # cCode = data[key]['code']
        cSubject =  'CS' # TODO: Remove this line when the full list of courses is used
        cCode = '123'    # TODO: Remove this line when the full list of courses is used
        cCredits = data[key]['credits']
        cDescription = data[key]['description'] 

        try:
            # Insert course into the database's courses table
            cursor.execute("INSERT INTO courses (cName, cSubject, cCode, cCredits, cDescription) VALUES (%s, %s, %s, %s, %s)", (cName, cSubject, cCode, cCredits, cDescription, ))
            conn.commit()
        except:
            print("Error inserting course into database")
            
    cursor.close()
    conn.close()
      
    pass


def PopProfessors():
    """
    Function to populate the professors table with all professors at UW-Madison.
    Entries contain a pUID, the professor's first name, last name, and data (where data is a dictionary of all rate my professor data).

    SAMPLE DATA: {'Fname': 'Peter', 'Lname': 'Adamczyk', 'dept': 'Mechanical Engineering', 'RMPID': 2215832, 'RMPRating': 4.9, 'RMPTotalRatings': 12, 'RMPRatingClass': 'good'}
    """
    uni = api.scrape_professors()

    # Iterating through every UW professor on RMP
    for key in uni:
        prof_json = {}                                           # Create a new JSON object for each professor
        professor = uni[key]                                     # Get the professor object
        prof_json['Fname'] = professor.first_name                # Get the professor's first name
        prof_json['Lname'] = professor.last_name                 # Get the professor's last name
        prof_json['dept'] = professor.department                 # Get the professor's department
        prof_json['RMPID'] = professor.ratemyprof_id             # Get the professor's RMP ID
        prof_json['RMPRating'] = professor.overall_rating        # Get the professor's RMP rating
        prof_json['RMPTotalRatings'] = professor.num_of_ratings  # Get the professor's total number of RMP ratings
        prof_json['RMPRatingClass'] = professor.rating_class

        # TODO: Insert each professor into the database's professors table

        print(prof_json)


    return True

def PopRedditComments():
    """
    Function to populate the rc (reddit comments) table with all comments that contain a specific keyword and are posted to r/UWMadison.
    Entries contain a commend ID, the comment's text, a link to the comment, the comment's upvotes, and the cUID of the course the comment is about.
    """
    search = '577'
    comments_json = []
    # # Search for comments that mention the substring provided by the user in r/UWMadison
    for submission in uwmadison_subreddit.search(search, limit=25):
        for comment in submission.comments:
            if search in comment.body:
                # Turn comment link, commend body, and number of upvotes into a dictionary
                comment_dict = {'link': reddit_url+comment.permalink, 'body': comment.body, 'upvotes': comment.score}
                # Add the dictionary to the list of comments
                comment_json = json.dumps(comment_dict)
                comments_json.append(comment_json)

    print(comments_json)
    pass

def PopTeaches(cName):
    """
    Function to populate the teaches table with cUIDs and pUIDs for each course. Defining what courses each professor teaches.
    Entries contain a cUID and a pUID.
    """
    search = cName
    grade_distributions = MadGrades(search)
    course_professors = []
    all_term_data = []

    # Iterate over all terms in the grade distribution data
    for i in range(len(grade_distributions["courseOfferings"])):
        single_term_data = grade_distributions["courseOfferings"][i]["sections"]
        all_term_data.append(single_term_data)

    # Iterate over all terms in the grade distribution data, and create a list of all professors that teach the course
    num_terms = len(all_term_data)
    for j in range(num_terms):
        for k in range(len(all_term_data[j])):
            course_professors.append(all_term_data[j][k]["instructors"])

    
    # TODO:
    # 1. Get the cUID of the course with course name = cName
    # 2. Get the pUID of the professor with professor name = course_professors[i]['name']
    # 3. Insert the tuple (cUID, pUID) into the teaches table
    # 4. Repeat for all courses at the UW-Madison

    pass

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
    PopCourses()
    # PopProfessors()
    # PopRedditComments()
    # PopTeaches("Introduction to Algorithms")
