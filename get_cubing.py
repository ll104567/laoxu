#!/usr/bin/env python3
# date:2020.6.13

from bs4 import BeautifulSoup
import requests_html

url = 'https://cubingchina.com/'
filename ='cubingchina.csv'

s = requests_html.HTMLSession()
a = s.get(url)
b = BeautifulSoup(a.text,'lxml')

title = []
author = []
date = []
text = []

# get title
for i in b.select('h3.panel-title'):
    title.append(i.text)

#get author
for i in b.select('span.author'):
    author.append(i.text)

#get_date
for i in  b.select('span.date'):
    date.append(i.text)

#get_text
for i in b.select('div.desc'):
    text.append(i.text.replace('\r\n','').replace('\n','').replace('\t',''))

for i in range(len(title)):
    print(date[i],title[i],author[i])
