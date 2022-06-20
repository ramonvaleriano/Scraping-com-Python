from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://alura-site-scraping.herokuapp.com/hello-world.php'

response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')

print(soup)
