from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

page = 'https://alura-site-scraping.herokuapp.com/index.php'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}

request = Request(page, headers=headers)
response = urlopen(request)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')

# Acessando os conteúdos das Tags
titulo = soup.html.head.title
print(titulo.text)
titulo1 = soup.title
print(titulo1.get_text('#', strip=True))
h5 = soup.h5.getText()
print(h5)
