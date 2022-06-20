from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://alura-site-scraping.herokuapp.com/index.php'

response = urlopen(url)
html = response.read().decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')
anuncios = soup.find('div', {'id': 'container-cards'}).findAll('div', class_='well card')

for anuncio in anuncios:

    print(anuncio)
    print('\n\n')