import time
import requests
from bs4 import BeautifulSoup

url = 'http://old.mindmanager.cn/muban/category_0/'
base_url = 'http://old.mindmanager.cn/'

def gene_url_pool(url):
    x = []
    for i in range(1,101):
        x.append('{}p{}.html'.format(url,i))
    return x

def get_abs_link(url):
    xxoo = []
    a = requests.get(url)
    b = BeautifulSoup(a.text,'lxml')
    for i in b.select('p.bg-1>a'):
        xxoo.append(i['href'])
    return xxoo

def combine_url(url_list,base_url):
    x = []
    for i in url_list:
        x.append(base_url+i)
    return x

if __name__ == '__main__':
    
    f = open('url.txt','w')

    url_data = gene_url_pool(url)
    for i in url_data:
        url_abs_link = get_abs_link(i)
        url_link = combine_url(url_abs_link,base_url)
        print('{} is ok...'.format(i))
        for j in url_link:
            f.write(j+'\n')
        time.sleep(1)

