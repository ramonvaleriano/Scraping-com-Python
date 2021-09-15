from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

url = 'https://alura-site-scraping.herokuapp.com/index.php'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

request = Request(url, headers=headers)
response = urlopen(request)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')
imagem1 = soup.img
print(imagem1.attrs)
print(imagem1.attrs.keys())
print(imagem1.attrs.values())
print(soup.img['class'])
print(imagem1.get('src '))