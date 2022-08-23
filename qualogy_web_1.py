from bs4 import BeautifulSoup
import requests
import urllib.request
from urllib.request import Request, urlopen
import re
import json
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


for link in links_list:
    if link==6:
        break
    try:
        req=Request(link)
        result=urlopen(req).read()
        doc_link=BeautifulSoup(result,'html.parser')
        title=doc_link.find(attrs={'class':'vacancy-title'})
        Exp=doc_link.find(attrs={'class':'vacancy-experience'})
        #job_text=doc_link.find('p')
        code=Exp.text
        name=title.text
        Exprince=code.replace('\n','')
        email="career@qualogy.com"
        dict_1={'Title':name,'Exprince':Exprince,'Email':email}
        name_list.append(dict_1)
    except:
        pass

print(name_list)

json_data= json.dumps(name_list)
with open("sample.json","a") as file:
    file.write(json_data)
'''
print('test')
        list_1=['Title Name',name]
        list_2=['Exprince',Exprince]
        list_3=['Email',Email]
'''
