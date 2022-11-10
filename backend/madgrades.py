import requests
import config

# Instantiate Madgrades API Token
madgrades_api_token = config.madgrades_api_token
auth_header = {'Authorization': 'Token ' + madgrades_api_token} # Authorization header, required for API call

# URL Constants
madGrades_course_url = 'https://api.madgrades.com/v1/courses/'
madGrades_query_url = madGrades_course_url +'?query='
reddit_url = 'https://www.reddit.com'

def MadGrades(courseCode):
    """
    Pulls grade distributions from every course at UW-Madison and populates the grade-distributions table
    """
    search = courseCode
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
    return(courses)