from bs4 import BeautifulSoup
from urllib.request import urlopen
from funcoes_tratando_scrap import (
    byte_string_parcial,
    byte_string_completa
)

url = 'https://alura-site-scraping.herokuapp.com/index.php'

response = urlopen(url)
html = response.read()

html_tratado1 = byte_string_completa(html)
html_tratado2 = byte_string_parcial(html)

print(html_tratado1)
print(html_tratado2)