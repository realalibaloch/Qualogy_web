from bs4 import BeautifulSoup
import requests
import urllib.request
from urllib.request import Request, urlopen
import re
links_list=[]
req=Request('https://www.qualogy.com/nl/werken-bij/corporate')
result= urlopen(req).read()
doc= BeautifulSoup(result,'html.parser')

links=doc.find_all('a')


for link in links:
    base='https://www.qualogy.com'
    url=link.get('href')
    print(url)
    links_list.append(url)

#print(links_list)
'''
for i in links_list:
    base='https://www.qualogy.com'
    req=requests.compat.urljoin(base,i)
    result= urlopen(req).read()
    doc_link=BeautifulSoup(result,'html.parser')
    print(doc_link)

#
title= doc.find_all(attrs={'class':'vacancy-title'})
for name in title:
    print(t.text)
'''
