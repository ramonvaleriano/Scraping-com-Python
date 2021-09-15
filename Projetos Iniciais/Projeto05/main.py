from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

url = 'https://alura-site-scraping.herokuapp.com/index.php'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

request = Request(url, headers=headers)

response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')
imagem = soup.find('img')
print(imagem)
imagens = soup.findAll('img')
print(imagens)
imagem1 = soup.findAll('img', limit=1)
print(imagem1)
hs = soup.findAll(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
print(hs)
p = soup.findAll('p')
print(p)
p_epecifico = soup.findAll('p', {'class':'txt-value'})
print(p_epecifico)
p_text = soup.findAll('p', text='Belo Horizonte - MG')
print(p_text)
p_bem_espeficico = soup.findAll('img', alt='Foto')
print(p_bem_espeficico)

for item in p_bem_espeficico:
    print(item.get('src'))

test_class = soup.findAll('p', class_='txt-value')
print(test_class)

test_text = soup.findAll(text=True)
print(test_text)