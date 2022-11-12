import unittest
import pytest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from app import db
from models.models import Courses, Professors, RC, Teaches

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
        """TODO Test madgrades api"""
        self.assertEqual(1, 1)
    
if __name__ == '__main__':
    unittest.main() # Run all unit tests
