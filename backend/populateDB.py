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
uwm_rmp_sid_1 = "1256"  # RMP School ID #1
uwm_rmp_sid_2 = "18418" # RMP School ID #2

api_1 = RateMyProfApi(uwm_rmp_sid_1, testing = True)
api_2 = RateMyProfApi(uwm_rmp_sid_2, testing = True)


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

    file = open('sample.json', 'r') # Open the JSON file containing all UW-Madison courses

    data = json.load(file) # Load the JSON file into a dictionary

    cursor = conn.cursor() # Create a cursor object to execute SQL queries

    # For each course in the dictionary, get all the courses fields and insert into the table
    for key in data.keys():
        cName = data[key]['name']
        cSubject =  data[key]['subject']
        cCode = data[key]['code']
        cCredits = data[key]['credits']
        cDescription = data[key]['description'] 
        cReq = data[key]['requisite']

        try:
            # Insert course into the database's courses table
            cursor.execute("INSERT INTO courses (cName, cSubject, cCode, cCredits, cDescription, cReq) VALUES (%s, %s, %s, %s, %s, %s)", (cName, cSubject, cCode, cCredits, cDescription, cReq,))
            conn.commit()
        except Exception as e:
            print(e)
            print("Error inserting course into database")
            
    cursor.close()
    conn.close()
    pass

def PopProfessorsHelper(endpoint):
    """
    Helper function to populate the professors table with all professors at UW-Madison.

    """

    cursor = conn.cursor() # Create a cursor object to execute SQL queries

    # Iterating through every UW professor on RMP
    for key in endpoint:
        prof_json = {}                                           # Create a new JSON object for each professor
        professor = endpoint[key]                                # Get the professor object
        prof_json['Fname'] = professor.first_name                # Get the professor's first name
        prof_json['Lname'] = professor.last_name                 # Get the professor's last name
        prof_json['dept'] = professor.department                 # Get the professor's department
        prof_json['RMPID'] = professor.ratemyprof_id             # Get the professor's RMP ID
        prof_json['RMPRating'] = professor.overall_rating        # Get the professor's RMP rating
        prof_json['RMPTotalRatings'] = professor.num_of_ratings  # Get the professor's total number of RMP ratings
        prof_json['RMPRatingClass'] = professor.rating_class
        pData = json.dumps(prof_json)                            # Convert the JSON object to a string

        try:
            # Insert course into the database's courses table
            cursor.execute("INSERT INTO professors (pFName, pLName, pData) VALUES (%s, %s, %s)", (prof_json['Fname'], prof_json['Lname'], pData))
            conn.commit()
        except Exception as e:
            print(e)
            print("Error inserting professor into database")
      
    cursor.close()

    pass

def PopProfessors():
    """
    Function to populate the professors table with all professors at UW-Madison. Iterates over the two RMP school IDs and calls the helper function to populate the table.
    Entries contain a pUID, the professor's first name, last name, and data (where data is a dictionary of all rate my professor data).

    SAMPLE DATA: {'Fname': 'Peter', 'Lname': 'Adamczyk', 'dept': 'Mechanical Engineering', 'RMPID': 2215832, 'RMPRating': 4.9, 'RMPTotalRatings': 12, 'RMPRatingClass': 'good'}
    """
    endpoints = []

    endpoints.append(api_1.scrape_professors())
    endpoints.append(api_2.scrape_professors())

    for endpoint in endpoints:
        PopProfessorsHelper(endpoint)
    pass

def PopRedditComments():
    """
    Function to populate the rc (reddit comments) table with all comments that contain a specific keyword and are posted to r/UWMadison.
    Entries contain a commend ID, the comment's text, a link to the comment, the comment's upvotes, and the cUID of the course the comment is about.
    """

    cursor = conn.cursor() # Create a cursor object to execute SQL queries

    # Query the courses table for the cCode and cUID of all courses
    cursor.execute("SELECT cUID, cName, cCode FROM courses WHERE cName Like 'Introduction to Algorithms'") # Get the cUID, cName, and cCode of all courses
    # cursor.execute("SELECT cUID, cName, cCode FROM courses WHERE cName Like 'PRINCIPLES OF BIOLOGICAL ANTHROPOLOGY'") # Get the cUID, cName, and cCode of all courses
    courses = cursor.fetchall() 

    # Iterate through every entry in courses
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

        # NEW METHOD: Searching for posts thathave either the full course code, or the courses acronym + course number (e.g. CS506 or CS 506)
        # TODO: Will need to continually refine how we choose comments to populate the DB with
        # Search for submissions that contain the course's code
        for submission in uwmadison_subreddit.search(search, limit=50):
            if search.lower() in submission.title.lower() or acronym + cNum in submission.title or acronym + ' ' + cNum in submission.title: # If the course's code is in the submission's title
                # print(submission.title) # Print the submission's title
                submission.comments.replace_more(limit=5) # Return only the top three comments from the comment tree
                for comment in submission.comments.list():
                    if (comment.score > 2 or cNum in comment.body) and len(comment.body) < 1000:
                        try:
                            # Insert reddit comment into the database's rc table
                            cursor.execute("INSERT INTO rc (cUID, comBody, comLink, comVotes) VALUES (%s, %s, %s, %s)", (course[0], comment.body, reddit_url+comment.permalink, comment.score,))
                            conn.commit()
                        except Exception as e:
                            print(e)
                            print("Error inserting reddit comment into database")


        # OLD METHOD: Our old plan was to search for comments that mentioned the course code/number. This is ineffective because a lot of posts have the course code 
        # in the title but not in the course comment body.

        # Search for comments that mention the substring provided by the user in r/UWMadison
        # for submission in uwmadison_subreddit.search(search, limit=25):
        #     for comment in submission.comments:
        #         if search in comment.body and comment.score > 5 and len(comment.body) < 1000:

        #             try:
        #                 # Insert reddit comment into the database's rc table
        #                 cursor.execute("INSERT INTO rc (cUID, comBody, comLink, comVotes) VALUES (%s, %s, %s, %s)", (course[0], comment.body, reddit_url+comment.permalink, comment.score,))
        #                 conn.commit()
        #             except Exception as e:
        #                 print(e)
        #                 print("Error inserting reddit comment into database")
            
    cursor.close()

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
    try:
        course_url = course_listings['results'][0]['url']                          # Get API Endpoint URL of first course in list
    except IndexError:
        return
    response = requests.get(course_url, headers=auth_header)                   # API call to get course data associated with select course
    full_course_data = response.json()                                  
    grades_url = full_course_data['gradesUrl']                                 # Get API Endpoint URL of grade distribution data                                            
    response = requests.get(grades_url, headers=auth_header)                   # API call to access grade distribution data
    courses = response.json()                                                  # Course offerings dictionary, with a list of dictionaries for each 
    print(courses)
    return(courses)

if __name__ == '__main__':
    # PopCourses()
    # PopProfessors()
    PopRedditComments()
    # PopTeaches("Introduction to Algorithms")
    # with open('sample.json') as data_file:    
    #     data = json.load(data_file)
    #     for v in data.values():
    #         print(v['code'])
    #         MadGrades(v['code'])
    # print(MadGrades("ACCT I S 301"))


    
