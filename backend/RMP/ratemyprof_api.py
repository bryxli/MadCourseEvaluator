import requests
import json
import math
import os
from .professor import Professor

class RateMyProfApi:
    """
    RateMyProfAPI class contains functions to scrape professor data from RateMyProfessors.com
    """
    def __init__(self, school_id):
        """
        Constructor for RateMyProfApi class.
        Args: school_id (int): ID of the UID that RateMyProfessor assigns to identify schools.
        """
        self.UniversityId = school_id
        

    def ScrapeProfessors(self, testing = False):  # creates List object that include basic information on all Professors from the IDed University
        """
        Scrapes all professors from the school with the given school_id. 
        Return: a list of Professor objects, defined in professor.py.
        """
        if testing:
            print("University ID: ", self.UniversityId)
        
        professors = dict() 
        num_of_prof = self.get_num_of_professors() # The number of professors with RMP records associated with this university school_id.
        
        if testing:
            print("Number of Professors Total: ", num_of_prof)

        num_of_pages = math.ceil(num_of_prof/20)   # The API returns 20 professors per page.
        for i in range(1, num_of_pages + 1):  # the loop insert all professor into list
            
            if self.UniversityId == '1256':
                page = requests.get(
                    "http://www.ratemyprofessors.com/filter/professor/?&page="
                    + str(i)
                    + "&queryoption=TEACHER&queryBy=schoolId&sid="
                    + str(self.UniversityId)
                )
            else:
                page = requests.get(
                    "http://www.ratemyprofessors.com/filter/professor/?&page="
                    + str(i)
                    + "&queryoption=TEACHER&query=*&sid="
                    + str(self.UniversityId)
                )
            
            json_response = json.loads(page.content)

            for json_professor in json_response["professors"]:
    
                # print(json_professor)
                professor = Professor(
                    json_professor["tid"],
                    json_professor["tFname"],
                    json_professor["tLname"],
                    json_professor["tNumRatings"],
                    json_professor["overall_rating"],
                    json_professor["rating_class"],
                    json_professor["tDept"]
                    )

                professors[professor.ratemyprof_id] = professor
                
        if testing:
            print("Professors actually added: ", str(len(professors)))

        return professors

    def get_num_of_professors(self):
        """
        Helper function to get the number of professors in the school with the given school_id.
        """
        if self.UniversityId == '1256':
            page = requests.get(
                "http://www.ratemyprofessors.com/filter/professor/?&page=1&queryoption=TEACHER&queryBy=schoolId&sid="
                + str(self.UniversityId)
            )
        else: 
            page = requests.get(
                "http://www.ratemyprofessors.com/filter/professor/?&page=1&queryoption=TEACHER&query=*&sid="
                + str(self.UniversityId)
            )

        temp_jsonpage = json.loads(page.content)
        num_of_prof = (temp_jsonpage["searchResultsTotal"]) 
        return num_of_prof