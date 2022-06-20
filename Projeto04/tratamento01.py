from bs4 import BeautifulSoup
from urllib.request import urlopen


url = 'https://alura-site-scraping.herokuapp.com/index.php'

response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')
#print(soup.html.prettify())
print(soup.header)
print('Colentando um dado ainda mais especifico:')
print(soup.header.li)
print(soup.header.li.get_text())
print(soup.head.title)
print(soup.head.title.get_text())
print(soup.div.div.div.div)
print(soup.div.div.div.div.h5)
print(soup.div.div.div.div.h5.get_text())
print(soup.div.div.div.div.h5.getText())