import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import re

url = 'https://guide.wisc.edu/courses/'
data = requests.get(url)

my_data = []

soup = BeautifulSoup(data.text, 'html.parser')
articles = soup.select('p')
weblist = []
open("sample.json", 'w').close()

#find courses web link
myuls = soup.findAll('ul', attrs={"class":"nav levelone"})
for ul in myuls: 
    for link in ul.find_all('a'):
        weblist.append(link.get('href'))
        
subjectList = []
for ul in myuls: 
    for link in ul.find_all('a'):
        subjectList.append(link.get_text().split(" (")[0])

#concat webname to get real link
webname_count_subject = 0
for webname in weblist: 

    url = 'https://guide.wisc.edu' + webname
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')

    i = 0
    j = 0
    my_dict = {}

    #find the informatin we want,like description, credits, name, last taught
    for link in soup.find_all('p'):
        current_dict = {}
        i = i + 1
        if i == 1:
            courses = link.get_text().replace(u'\xa0', u'').replace(u'\u200b', u'').replace(u'\xa9', u'').replace(u'\u2022', u'').replace(u'\n', u'').replace(u'\u2014', u'').split("  ", 1)
            courseCode = re.split('(\d+)',courses[0]) #use re to split character and strings
            my_dict['code'] = courseCode[0] + " " + courseCode[1]
            my_dict['name'] = courses[1]
            my_dict['subject'] = subjectList[webname_count_subject]
            #print(my_dict['name'])

        if i == 2 : 
            my_dict['credits'] = link.get_text().replace(u'\xa0', u'').replace(u'\u200b', u'').replace(u'\xa9', u'').replace(u'\u2022', u'').replace(u'\u2014', u'')[:-1]

        if i == 3 : 
            my_dict['description'] = link.get_text().replace(u'\xa0', u'').replace(u'\u200b', u'').replace(u'\xa9', u'').replace(u'\u2022', u'').replace(u'\n', u'').replace(u'\u2014', u'')

        if i == 4 : 
            my_dict['requisite'] = link.get_text().replace(u'\xa0', u'').replace(u'\u200b', u'').replace(u'\xa9', u'').replace(u'\u2022', u'').replace(u'\u2014', u'')


        
        if 'Last Taught' in link.get_text().replace(u'\xa0', u'').replace(u'\u200b', u'').replace(u'\xa9', u'').replace(u'\u2022', u'').replace(u'\u2014', u''):
            my_dict['last taught'] = link.get_text().replace(u'\xa0', u'').replace(u'\u200b', u'').replace(u'\xa9', u'').replace(u'\u2022', u'').replace(u'\u2014', u'')
            i = 0
            j = j + 1
            current_dict[f'{webname[9:-1]} {j}']   = my_dict
            #close the file after attaching
            with open("sample.json", "a") as outfile:
                json.dump(current_dict,  outfile, indent = 4)
            outfile.close()

    webname_count_subject = webname_count_subject + 1
