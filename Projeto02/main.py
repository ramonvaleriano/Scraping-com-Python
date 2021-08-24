from urllib.request import urlopen
from bs4 import BeautifulSoup

url1 = 'https://alura-site-scraping.herokuapp.com/index.php'

response1 = urlopen(url1)
html1 = response1.read()
soup1 = BeautifulSoup(html1, 'html.parser')

