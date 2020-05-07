import requests
from bs4 import BeautifulSoup

star_data = {"star-rating Four":4,
        'star-rating One':1,
        'star-rating Two':2,
        'star-rating Three':3,
        'star-rating Five':5,
        }

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
        price = float(xxoo.select('p.price_color')[0].text[2:])
        title = xxoo.h3.a['title'] 
        star = ' '.join(xxoo.p['class'])
        star_number = star_data.get(star,0)

        price_title_star.append([price,star_number,title])

#store
with open('price_star_title.txt','w') as f:
    for i in price_title_star:
        f.write('{}\t{}\t{}\n'.format(i[0],i[1],i[2]))

# sort money
x = sorted(price_title_star,key=lambda x:x[0])[::-1][:10]

#sort star
y = sorted(price_title_star,key=lambda x:x[1])[::-1][:10]

#print  money
for i in x:
    print(i)

#sep
print('==='*20)

#print  star
for i in y:
    print(i)
