import requests
from bs4 import BeautifulSoup


# get page number
page_tmp = requests.get('http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html')
page_bs  = BeautifulSoup(page_tmp.text,'lxml')
page_number = int(page_bs.find_all(class_="current")[0].text.split()[-1])

#define a data stru

price_title_star = []

# for loop to get page

for i in range(1,page_number+1):
    current_page = requests.get('http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-{}.html'.format(i))
    current_bs = BeautifulSoup(current_page.text,'lxml')
    print('{} page ...'.format(i))

    for xxoo in current_bs.select('article'): 
        price = xxoo.select('p.price_color')[0].text[2:] 
        title = xxoo.h3.a['title'] 
        star = ' '.join(xxoo.p['class'])
        
        price_title_star.append([price,title,star])

# sort

x = sorted(price_title_star,key=lambda x:x[0])[::-1][:10]

#print

for i in x:
    print('\t'.join(i))


