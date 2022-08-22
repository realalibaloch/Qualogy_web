from bs4 import BeautifulSoup
import requests
import urllib.request
from urllib.request import Request, urlopen
import re
links_list=[]
req=Request('https://www.qualogy.com/nl/werken-bij/corporate')
result= urlopen(req).read()
doc= BeautifulSoup(result,'html.parser')

for content in doc.find_all(attrs={'class':'vacancy-content'}):
    print(content.text)
links=doc.find_all('a')


for link in links:
    url=link.get('href')
    links_list.append(url)

#print(links_list)
'''
for content in doc:
    name=doc.find_all(class_='vacancy-title')
    


for name in title:
    print(name.text)
job_code=doc.find_all(attrs={'class':'vacancy-location-label'})
for job_c in job_code:
    print(job_c.text)
'''
