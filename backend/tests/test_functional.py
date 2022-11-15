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

    
    
if __name__ == '__main__':
    unittest.main() # Run all unit tests
    # TestUtil().test_madgrades_api() # Run specific unit test
