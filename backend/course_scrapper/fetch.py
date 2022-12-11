#!/usr/bin/python3
import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = 'https://guide.wisc.edu/courses/acct_i_s/'
data = requests.get(url)

my_data = []

soup = BeautifulSoup(data.text, 'html.parser')
articles = soup.select('p')

f = open("all.txt", "w")
i = 0
j = 0
my_dict = {}
nested_dict = {}

for link in soup.find_all('p'):
    current_dict = {}
    #print(link.get_text())        
    #if i == 0:
    #   f.write(link.get_text().replace(u'\xa0', u'').replace(u'\u200b', u'').replace(u'\xa9', u'').replace(u'\u2022', u''))

    #f.writelines('\n')
    #i = i +1

    #if 'Last Taught' in link.get_text().replace(u'\xa0', u'').replace(u'\u200b', u'').replace(u'\xa9', u'').replace(u'\u2022', u''):
    #    i = 0
    i = i + 1

    if i == 1:
        my_dict['name'] = link.get_text().replace(u'\xa0', u'').replace(u'\u200b', u'').replace(u'\xa9', u'').replace(u'\u2022', u'').replace(u'\n', u'').replace(u'\u2014', u'')
        #print(my_dict['name'])

    if i == 2 : 
        my_dict['credits'] = link.get_text().replace(u'\xa0', u'').replace(u'\u200b', u'').replace(u'\xa9', u'').replace(u'\u2022', u'').replace(u'\n', u'').replace(u'\u2014', u'')

    if i == 3 : 
        my_dict['description'] = link.get_text().replace(u'\xa0', u'').replace(u'\u200b', u'').replace(u'\xa9', u'').replace(u'\u2022', u'').replace(u'\n', u'').replace(u'\u2014', u'')

    if i == 4 : 
        my_dict['requisite'] = link.get_text().replace(u'\xa0', u'').replace(u'\u200b', u'').replace(u'\xa9', u'').replace(u'\u2022', u'').replace(u'\n', u'').replace(u'\u2014', u'')


    
    if 'Last Taught' in link.get_text().replace(u'\xa0', u'').replace(u'\u200b', u'').replace(u'\xa9', u'').replace(u'\u2022', u'').replace(u'\n', u'').replace(u'\u2014', u''):
        my_dict['last taught'] = link.get_text().replace(u'\xa0', u'').replace(u'\u200b', u'').replace(u'\xa9', u'').replace(u'\u2022', u'').replace(u'\n', u'').replace(u'\u2014', u'')
        i = 0
        j = j + 1
        current_dict[f'class{j}']   = my_dict
        #nested_dict.update(current_dict)
        with open("test_file.json", "a") as outfile:
            json.dump(current_dict,  outfile, indent = 4)
        outfile.close()
        break


        #print(nested_dict[f'class{j}'] )
#print(my_dict)


#pretty = json.dumps(nested_dict, indent = 4)
#print(pretty)
#f.close()










    #print(soup.find('p', class_="courseblockdesc noindent").text)  #description
    #print(link.find('strong').text)
    #print(soup.find('span', class_="courseblockcode").text)
    #print(link.find('span').text)
    #print(link.find('span', class_="cbextra-data").text) #credit

    #print(link.find(class_="courseblockdesc noindent").text)


    #print(link.get_text())
    #print(link)
# for article in articles:

#     title = article.get_text()

    #my_data.append({"title": title})

#print(soup.p)

# #!/usr/bin/python3
# import requests

# url = 'https://guide.wisc.edu/courses/acct_i_s/'

# data = requests.get(url)

# print(data.text)