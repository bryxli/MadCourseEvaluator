import requests
import json
import unittest
import pytest
import os
import sys
import inspect
import json

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from app import app

"""
# Functional Unit Tests: View Functions respond to nominal and non-nominal inputs (e.g. 404, 500, 200, etc.)
"""

class TestCourseRoutes(unittest.TestCase):
    """
    Tests for DB Models
    """
    def test_all_courses(self): 
        request = app.test_client().get('/all-courses')   # Make a request to the /all-courses endpoint
        self.assertEqual(request.status_code, 200)        # Assert that the request was successful (200)
        self.assertEqual(request is not None, True)       # Assert that the request is not None
        self.assertEqual(request.json is not None, True)  # Assert that the request.json is not None

        # Assert that the first 5 courses contain all fields
        i = 0
        for key in request.json.keys():
            self.assertEqual(request.json[key]['cUID'] is not None, True)
            self.assertEqual(request.json[key]['cName'] is not None, True)
            self.assertEqual(request.json[key]['cCode'] is not None, True)
            self.assertEqual(key, str(request.json[key]['cUID']))
            i += 1
            if i == 5:
                break

    def test_all_profs(self): 
        request = app.test_client().get('/all-profs')     # Make a request to the /all-courses endpoint
        self.assertEqual(request.status_code, 200)        # Assert that the request was successful (200)
        self.assertEqual(request is not None, True)       # Assert that the request is not None
        self.assertEqual(request.json is not None, True)  # Assert that the request.json is not None

        # Assert that the first 5 courses contain all fields
        i = 0
        for key in request.json.keys():
            self.assertEqual(request.json[key] is not None, True)
            self.assertEqual(request.json[key]['name'] is not None, True)
            self.assertEqual(request.json[key]['dept'] is not None, True)
            # self.assertEqual(key, str(request.json[key]['RMPID'])) # We may want to make it so we are returning the pUID for each professor too
            self.assertEqual("RMPID" in request.json[key].keys(), True)
            self.assertEqual("RMPRating" in request.json[key].keys(), True)
            self.assertEqual("RMPRatingClass" in request.json[key].keys(), True)
            self.assertEqual("RMPTotalRatings" in request.json[key].keys(), True)
            i += 1
            if i == 5:
                break

    def test_course_info(self):
        cs577_cUID = "58786" 
        route = '/course-info/'
        full_request = route + cs577_cUID
        request = app.test_client().get(full_request)     # Make a request to the /course-info/58786 endpoint
        self.assertEqual(request.status_code, 200)        # Assert that the request was successful (200)

        # Assert the json contains all keys
        self.assertEqual("cUID" in request.json.keys(), True)
        self.assertEqual("cName" in request.json.keys(), True)
        self.assertEqual("cCode" in request.json.keys(), True)
        self.assertEqual("cDescription" in request.json.keys(), True)
        self.assertEqual("cReq" in request.json.keys(), True)
        self.assertEqual("cCredits" in request.json.keys(), True)
        self.assertEqual("cSubject" in request.json.keys(), True)

        # Assert that the course info contains all required fields
        self.assertEqual(request.json['cUID'] is not None, True)
        self.assertEqual(request.json['cName'] is not None, True)
        self.assertEqual(request.json['cCode'] is not None, True)

        # Assert that the JSON returned contains only data from one course (7 keys total per course)
        self.assertEqual(len(request.json.keys()), 7)

    def test_course_profs(self):
        cs577_cUID = "58786" 
        route = '/course-profs/'
        full_request = route + cs577_cUID
        request = app.test_client().get(full_request)     # Make a request to the /course-info/58786 endpoint
        self.assertEqual(request.status_code, 200)        # Assert that the request was successful (200)

        # Assert the json contains at least one key
        self.assertEqual(len(request.json.keys()) > 0, True)

        # Assert that every professor entry contains all keys (6 total) and required fields (3)
        contains_marc_renault = False
        contains_eric_bach = False
        for key in request.json.keys():
            self.assertEqual("name" in request.json[key].keys(), True)
            self.assertEqual("dept" in request.json[key].keys(), True)
            self.assertEqual("RMPID" in request.json[key].keys(), True)
            self.assertEqual("RMPRating" in request.json[key].keys(), True)
            self.assertEqual("RMPRatingClass" in request.json[key].keys(), True)
            self.assertEqual("RMPTotalRatings" in request.json[key].keys(), True)
            self.assertEqual("name" in request.json[key].keys(), True)
            self.assertEqual("dept" in request.json[key].keys(), True)
            self.assertEqual("RMPID" in request.json[key].keys(), True)
            self.assertEqual(request.json[key]['name'] is not None, True)
            self.assertEqual(request.json[key]['dept'] is not None, True)
            self.assertEqual(request.json[key]['RMPID'] is not None, True)
            if request.json[key]['name'] == "Marc Renault":
                contains_marc_renault = True
            if request.json[key]['name'] == "Eric Bach":
                contains_eric_bach = True

        # Assert that the JSON returned contains at least the two known professors for this course
        self.assertEqual(contains_marc_renault, True)
        self.assertEqual(contains_eric_bach, True)

    def test_course_reddit_comments(self):
        cs577_cUID = "58786" 
        route = '/reddit-comments/'
        full_request = route + cs577_cUID
        request = app.test_client().get(full_request)     # Make a request to the /course-info/58786 endpoint
        self.assertEqual(request.status_code, 200)        # Assert that the request was successful (200)

        # Assert the json contains at least one key
        self.assertEqual(len(request.json.keys()) > 0, True)

        # Assert that every professor entry contains all keys (3 total) and required fields (3)
        i=0
        for key in request.json.keys():
            if i == 1:
                break
            i += 1
            self.assertEqual("comBody" in request.json[key].keys(), True)
            self.assertEqual("comLink" in request.json[key].keys(), True)
            self.assertEqual("comVotes" in request.json[key].keys(), True)
            self.assertEqual(request.json[key]['comBody'] is not None, True)
            self.assertEqual(request.json[key]['comLink'] is not None, True)
            self.assertEqual(request.json[key]['comVotes'] is not None, True)

            # Assert that the link is a valid URL
            self.assertEqual(request.json[key]['comLink'].startswith("https://"), True)

            # Make a request to the link and assert that it is a valid URL (200)
            link_request = requests.get(request.json[key]['comLink'])
            self.assertEqual(link_request.status_code, 200)

    # TODO: We are getting an error when loading the professors names, for some instances 
    # request.json['courseOfferings'][info]['sections'][section]['instructors'][0]['name'] 
    # is returning more than one name. I believe this is a bug in the MadGrades API itself,
    # but we should look into it further.
    def test_course_grade_distribution(self):
        cs577_cUID = "58786" 
        route = '/grade-distribution/'
        full_request = route + cs577_cUID
        request = app.test_client().get(full_request)     # Make a request to the /course-info/58786 endpoint
        self.assertEqual(request.status_code, 200)        # Assert that the request was successful (200)

        # Assert the json contains at least one key
        self.assertEqual(len(request.json.keys()) > 0, True)

        # Assert that JSON contains expected keys
        self.assertEqual('courseOfferings' in request.json.keys(), True)
        self.assertEqual('courseUuid' in request.json.keys(), True)
        self.assertEqual('cumulative' in request.json.keys(), True)

        # Assert that the per term course grade distribution data for courseOfferings contains expected keys
        for info in request.json['courseOfferings']:
            self.assertEqual('cumulative' in info.keys(), True)
            self.assertEqual('sections' in info.keys(), True)
            self.assertEqual('termCode' in info.keys(), True)

            # Assert that the per section course grade distribution data for courseOfferings contains instructors key with id and name for professor
            prof_list = []
            for section in range(len(info['sections'])):
                # print(info['sections'][section]['instructors'])
                self.assertEqual(info['sections'][section]['instructors'][0]['id'] is not None, True)
                self.assertEqual(info['sections'][section]['instructors'][0]['name'] is not None, True)
                prof_list.append(info['sections'][section]['instructors'][0]['name'].lower().strip())


            # Assert that the JSON returned contains at least the two known professors for this course
            # print(prof_list)
            # self.assertEqual('marc renault' in prof_list, True)
            # self.assertEqual('eric bach' in prof_list, True)





if __name__ == '__main__':
    unittest.main() # Run all unit tests