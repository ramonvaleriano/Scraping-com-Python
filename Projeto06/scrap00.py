from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://alura-site-scraping.herokuapp.com/index.php'

response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')
img01 = soup.find('img')
print(img01)
img_list01 = soup.findAll('img')
print(img_list01)
img_list01_limti01 = soup.findAll('img', limit=1)
print(img_list01_limti01)
img_list02 = soup.findAll(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
print(img_list02)
img_list03 = soup.findAll('p', {'class':'txt-value'})
print(img_list03)
img_list04 = soup.findAll('p', text='Belo Horizonte - MG')
print(img_list04)
img_list05 = soup.findAll('img', alt='Foto')
print(img_list05)
for item in img_list05:
    print(item.get('src'))
img_list06 = soup.findAll('p', class_='txt-value')
print(img_list06)
img_list07 = soup.findAll(text=True)
print(img_list07)