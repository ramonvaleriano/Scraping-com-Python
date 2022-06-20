from bs4 import BeautifulSoup
from urllib.request import urlopen
from funcoes_tratando_scrap import byte_string_parcial

url = 'https://alura-site-scraping.herokuapp.com/index.php'

response = urlopen(url)
html = response.read()

html = byte_string_parcial(html)
soup = BeautifulSoup(html, 'html.parser')

print(soup.find('h5').find_parent('div'))
print(soup.find('h5').find_parents())
print(soup.find('h5').find_parents('div'))
print(soup.find('h5').findNextSibling())
print(soup.find('h5').findPrevious())
print(soup.find('h5').findPreviousSiblings())
print(soup.find('h1').findNext())
print(soup.find('h5').findPrevious())
print(soup.find('h5').findAllNext())