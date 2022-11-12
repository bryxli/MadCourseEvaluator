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

# Unit Tests: DB Models, Utility Functions called by View Functions
def test_new_course():
    # Create a new course
    new_course = Courses(1, 'Intro to Computer Science', 'Computer Science', 'CS 101', '3', 'Intro to Computer Science', 'None')

    # Correct Input
    assert new_course.cUID == 1
    assert new_course.cName == 'Intro to Computer Science'
    assert new_course.cSubject == 'Computer Science'
    assert new_course.cCode == 'CS 101'
    assert new_course.cCredits == '3'
    assert new_course.cDescription == 'Intro to Computer Science'
    assert new_course.cReq == 'None'

    print('test_new_course() passed')
    
    # Functional Tests: View Functions respond to nominal and non-nominal inputs (e.g. 404, 500, 200, etc.)
    # Invalid Inputs

if __name__ == '__main__':
    test_new_course()