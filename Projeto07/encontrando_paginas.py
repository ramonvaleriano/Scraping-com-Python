from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://alura-site-scraping.herokuapp.com/index.php'

response = urlopen(url)
html = response.read().decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')
paginas = int(soup.find('span', class_='info-pages').get_text().split()[-1])
print(paginas)