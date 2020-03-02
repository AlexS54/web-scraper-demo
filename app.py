import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.emag.ro/laptopuri/c?ref=hp_menu_quick-nav_1_1&type=category')
soup = BeautifulSoup(r.text, 'html.parser')
f=open("output.txt", "w")

itemList=soup.select('#card_grid > .card-item')

for item in itemList:
    f.write(item['data-name']+'\n   '+item.select_one('.product-new-price').get_text()[:-6] + '\n')