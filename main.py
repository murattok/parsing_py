import requests
from bs4 import BeautifulSoup

base_url = 'https://dominopizza.ru/'
response = requests.get(base_url, verify=False)
soup = BeautifulSoup(response.text,'html.parser')

pizza_snacks = soup.find('div',{'id':'zakuski'})
pizza_snacks_menu = pizza_snacks.find_all('div',{'class':'col'})
pizza_snacks_list = []

for snacks in pizza_snacks_menu:
    snacks_content = snacks.a.div.find('div', {'class':'product-card-content'})
    snacks_content_name = snacks_content.find('div', {'class':'product-name'})
    snacks_content_description = snacks_content.find('div', {'class':'description-container'})
    snacks_content_price = snacks_content.find('div', {'class':'price'})
    snacks_content_picture = snacks.a.div.find('div', {'class':'product-picture'})

    pizza_snacks_list.append({
        'name': snacks_content_name.get_text(),
        'description': snacks_content_description.get_text(),
        'price': snacks_content_price.get_text(),
        'picture_url': snacks_content_picture.img.get('src')
     })
    
print('ЗАКУСКИ')
for snacks in pizza_snacks_list:
    print('==========================================================================')
    print(f'Название: {snacks["name"]}')
    print(f'Состав: {snacks["description"]}')
    print(f'Цена: {snacks["price"]}')
    print(f'Ссылка на картинку: {snacks["picture_url"]}')
    print('==========================================================================')

