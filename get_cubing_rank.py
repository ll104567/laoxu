import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://cubingchina.com/results/person/2017HUSH01'

data_stru = []

#get page
rsp = response =urllib.request.urlopen(url)
page_bs = BeautifulSoup(rsp.read(),'lxml')

#get table title
tmp = []
for i in page_bs.select('div#yw0')[0].select('th'):
    tmp.append(i.text.strip())
data_stru.append(tmp)

#get table data
for i in page_bs.select('div#yw0')[0].select('tr')[1:]:
    tmp = []
    for j in i.select('td'):
        tmp.append(j.text.strip())
    data_stru.append(tmp)

#print
for i in data_stru:
    print('\t'.join(i[:8]))

