from bs4 import BeautifulSoup
import requests
import urllib.request
from urllib.request import Request, urlopen
import re
links_list=[]
req=Request('https://www.qualogy.com/nl/werken-bij/corporate')
result= urlopen(req).read()
doc= BeautifulSoup(result,'html.parser')

links_list=[]
name_list=[]
for link in doc.find_all('a', href=True):
    if 'https://www.qualogy.com' not in link['href']:
        x=('https://www.qualogy.com'+link['href'])
        links_list.append(x)
    elif 'http' not in link['href']:
        z=0
        
        #print("Found the URL:", 'https://'+link['href'])
    else:
        z=0
        #print("Found the URL:", link['href'])




print(links_list)

for link in links_list:
    try:
        req=Request(link)
        result=urlopen(req).read()
        doc_link=BeautifulSoup(result,'html.parser')
        #title=doc_link.find('',attrs={'class':'vacancy-title'})
        title=doc_link.find(attrs={'class':'vacancy-title'})
        job_code=doc_link.find(attrs={'class':'vacancy-location-label'})
        print(job_code.text)
        name=title.text
        name_list.append(name)
        #print(doc_link)
    except:
        pass

#print(name_list)
