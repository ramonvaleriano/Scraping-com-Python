from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://alura-site-scraping.herokuapp.com/index.php'

# Tudo isso aqui será subtituido por uma função
responde = urlopen(url)
html = responde.read()
print(type(html))
html = html.decode('utf-8')
print(type(html))
html = ' '.join(html.split())
print(html)
html = html.replace('> <', '><')
print(html)

# Criando um função para faze esse tratamento
def tratando_html(html):

    html_tratado = html.decode('utf-8')
    html_tratado = ' '.join(html_tratado.split()).replace('> <', '><')

    return html_tratado

response = urlopen(url)
html = response.read()
html_novo = tratando_html(html)

print(html_novo)

soup = BeautifulSoup(html_novo, 'html.parser')
print(soup)

response2 = urlopen(url)
html2 = response2.read()

soup2 = BeautifulSoup(html2, 'html.parser')
print(soup2)

response3 = urlopen(url)
html3 = response3.read()

html3 = html3.decode('utf-8')

soup3 = BeautifulSoup(html3, 'html.parser')
print(soup3)
