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
current_dict = {}

for webname in weblist: 

    url = 'https://guide.wisc.edu' + webname
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')

    i = 0
    j = 0
    
    count = 0
    for link in soup.find_all('p'):
        if 'Last Taught' in link.get_text().replace(u'\xa0', u'').replace(u'\u200b', u'').replace(u'\xa9', u'').replace(u'\u2022', u'').replace(u'\u2014', u''):
            count = count + 1

    #find the informatin we want,like description, credits, name, last taught
    for link in soup.find_all('p'):
        
        i = i + 1
        if i == 1:
            courses = link.get_text().replace(u'\u200b', u'').replace(u'\xa9', u'').replace(u'\u2022', u'').replace(u'\n', u'').replace(u'\u2014', u'').split("  ", 1)
            courseCode = re.split('(\d+)',courses[0]) #use re to split character and strings
            current_dict[f'{webname[9:-1]} {j}'] = {}
            current_dict[f'{webname[9:-1]} {j}']['code'] = courseCode[0].replace(u'\xa0', u' ') + courseCode[1]
            current_dict[f'{webname[9:-1]} {j}']['name'] = courses[1]
            current_dict[f'{webname[9:-1]} {j}']['subject'] = subjectList[webname_count_subject]

        if i == 2 : 
            current_dict[f'{webname[9:-1]} {j}']['credits'] = link.get_text().replace(u'\xa0', u'').replace(u'\u200b', u'').replace(u'\xa9', u'').replace(u'\u2022', u'').replace(u'\u2014', u'')[:-1]

        if i == 3 : 
            current_dict[f'{webname[9:-1]} {j}']['description'] = link.get_text().replace(u'\xa0', u'').replace(u'\u200b', u'').replace(u'\xa9', u'').replace(u'\u2022', u'').replace(u'\n', u'').replace(u'\u2014', u'')

        if i == 4 : 
           current_dict[f'{webname[9:-1]} {j}']['requisite'] = link.get_text().replace("Requisites: ", "").replace(u'\xa0', u'').replace(u'\u200b', u'').replace(u'\xa9', u'').replace(u'\u2022', u'').replace(u'\u2014', u'')


        
        if 'Last Taught' in link.get_text().replace(u'\xa0', u'').replace(u'\u200b', u'').replace(u'\xa9', u'').replace(u'\u2022', u'').replace(u'\u2014', u''):
            current_dict[f'{webname[9:-1]} {j}']['last taught'] = link.get_text().replace(u'\xa0', u'').replace(u'\u200b', u'').replace(u'\xa9', u'').replace(u'\u2022', u'').replace(u'\u2014', u'')
            i = 0
            j = j + 1
        
        if j == count:
            break
            #close the file after attaching        
    webname_count_subject = webname_count_subject + 1

with open("sample.json", "a") as outfile:
    json.dump(current_dict,  outfile, indent = 4)
outfile.close()
