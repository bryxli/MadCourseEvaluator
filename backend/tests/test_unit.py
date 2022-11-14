import unittest
import pytest
import os
import sys
import inspect
import json

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from app import db
from models.models import Courses, Professors, RC, Teaches
import madgrades as mg
from RMP.ratemyprof_api import RateMyProfApi

"""
# Unit Tests: DB Models, Utility Functions called by View Functions
"""

class TestModels(unittest.TestCase):
    """
    Tests for DB Models
    """
    def test_models_new_course(self): 
        """Test new course creation"""
        new_course = Courses(1, 'Intro to Computer Science', 'Computer Science', 'CS 101', '3', 'Intro to Computer Science', 'None')
        self.assertEqual(new_course.cUID, 1)
        self.assertEqual(new_course.cName, 'Intro to Computer Science')
        self.assertEqual(new_course.cSubject, 'Computer Science')
        self.assertEqual(new_course.cCode, 'CS 101')
        self.assertEqual(new_course.cCredits, '3')
        self.assertEqual(new_course.cDescription, 'Intro to Computer Science')
        self.assertEqual(new_course.cReq, 'None')
        return True

    def test_models_new_prof(self):
        """Test new prof creation"""
        new_prof= Professors(1, 'Good Prof', '{"name": "Good Prof", "dept": "African Studies", "RMPID": 2623431, "RMPRating": 2.0, "RMPTotalRatings": 1, "RMPRatingClass": "poor"}')
        self.assertEqual(new_prof.pUID, 1)
        self.assertEqual(new_prof.pName,'Good Prof')
        self.assertEqual(new_prof.pData, '{"name": "Good Prof", "dept": "African Studies", "RMPID": 2623431, "RMPRating": 2.0, "RMPTotalRatings": 1, "RMPRatingClass": "poor"}')
        return True
    
    def test_models_new_RC(self):
        """Test new reddit comment creation"""
        comID = 1
        comBody = "This is a comment!"
        comLink = "https://www.reddit.com/r/UWMadison/comments/wabbh9/taking_chem_109_math_221_and_econ_101_first/ihztopb/"
        comVotes = 13
        cUID = 10101
        new_reddit_comment = RC(comID, comBody, comLink, comVotes, cUID)
        self.assertEqual(new_reddit_comment.comID, 1)
        self.assertEqual(new_reddit_comment.comBody, "This is a comment!")
        self.assertEqual(new_reddit_comment.comLink, "https://www.reddit.com/r/UWMadison/comments/wabbh9/taking_chem_109_math_221_and_econ_101_first/ihztopb/")
        self.assertEqual(new_reddit_comment.comVotes, 13)
        self.assertEqual(new_reddit_comment.cUID, 10101)
        return True

    def test_models_new_teaches(self):
        """Test new teaches entry creation"""
        new_teaches_entry = Teaches(1, 2, 3)
        self.assertEqual(new_teaches_entry.tUID, 1)
        self.assertEqual(new_teaches_entry.pUID, 2)
        self.assertEqual(new_teaches_entry.cUID, 3)
        return True
    

class TestUtil(unittest.TestCase):

    def test_madgrades_api(self):
        """Test that madgrades.py returns the correct grade distribution data for CS 577"""

        compsci_577_cCode = 'COMP SCI 577' 
        
        grade_distributions = mg.MadGrades(compsci_577_cCode) # Get grade distributions for COMP SCI 577

        # Test that grade distributions are returned with correct keys
        self.assertIsInstance(grade_distributions, dict)
        keys = list(grade_distributions.keys())
        self.assertEqual(keys, ['courseUuid', 'cumulative', 'courseOfferings'])

        # Check that the cumulative grade distribution is returned with correct keys
        self.assertIsInstance(grade_distributions['cumulative'], dict)
        cumulative_cols = ['total', 'aCount', 'abCount', 'bCount', 'bcCount', 'cCount', 'dCount', 'fCount', 'sCount', 'uCount', 'crCount', 'nCount', 'pCount', 'iCount', 'nwCount', 'nrCount', 'otherCount']
        keys = list(grade_distributions['cumulative'].keys())
        self.assertEqual(keys, cumulative_cols)

    def test_RMP_api(self):
        """Test that ratemyprof_api.py returns the expected professor data for each professor"""

        # Instantiate UW-Madison RateMyProfessor Object (DOCS: 1.1.2.1)
        uwm_rmp_sid_1 = "1256"  # RMP School ID #1
        uwm_rmp_sid_2 = "18418" # RMP School ID #2

        api_1 = RateMyProfApi(uwm_rmp_sid_1) # (DOCS: 1.1.2.2)
        # api_2 = RateMyProfApi(uwm_rmp_sid_2)

        professor_data = []

        # professor_data.append(api_1.ScrapeProfessors()) 
        # professors_data.append(api_2.ScrapeProfessors())

        # self.assertEqual(len(professor_data), 4243)
        # prof_json = {}                                   
        # print("professor = ",professor_data[0].keys())         
     
        # prof_json['name'] = professor.first_name + " " + professor.last_name 
        # prof_json['dept'] = professor.department              
        # prof_json['RMPID'] = professor.ratemyprof_id          
        # prof_json['RMPRating'] = professor.overall_rating        
        # prof_json['RMPTotalRatings'] = professor.num_of_ratings 
        # prof_json['RMPRatingClass'] = professor.rating_class
        # pData = json.dumps(prof_json)  # Convert the JSON object to a string

    
if __name__ == '__main__':
    unittest.main() # Run all unit tests
    # TestUtil().test_madgrades_api() # Run specific unit test
