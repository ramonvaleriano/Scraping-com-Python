from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def cria_request_inicial(url, headers):

    return Request(url, headers=headers)

def tratando_html(html):

    return html.decode('utf-8')

def criando_html(request):
    response = urlopen(request)
    html = response.read()
    return html

url = 'https://alura-site-scraping.herokuapp.com/index.php'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}

request = cria_request_inicial(url, headers)
html = criando_html(request)
html_tratado = tratando_html(html)

soup = BeautifulSoup(html_tratado, 'html.parser')
print(soup)
