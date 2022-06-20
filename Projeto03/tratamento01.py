from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://alura-site-scraping.herokuapp.com/index.php'

response = urlopen(url)
html = response.read()

print(html)
print(type(html))

html = html.decode('utf-8')
print(type(html))
print(html)

html = ' '.join(html.split())
print(html)

html = html.replace('> <', '><')
print(html)