from bs4 import BeautifulSoup
import requests
import urllib.request
from urllib.request import Request, urlopen
import re

link_list=[]
req= Request('https://www.qualogy.com/nl/werken-bij/corporate')
result=urlopen(req).read()
doc=BeautifulSoup(result,'html.parser')


link=doc.find_all('a')
for links in link:
    try:
        x=links.get('href')
        link_list.append(x)
    except:
        pass

print(link_list)
for i in link_list:
    try:
        req=Request(i)
        result=urlopen(i).read()
        doc_link=BeautifulSoup(result,'html.parser')
        #print(doc_link)
        title=doc_link.find(attrs={'class':'vacancy-title'})
        print(title)
    except:
        pass
