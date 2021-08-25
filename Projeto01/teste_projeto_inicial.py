from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://alura-site-scraping.herokuapp.com/hello-world.php'

# Response da requisição que fizemos ao cite.
response = urlopen(url)
html = response.read()
print(html)

soup = BeautifulSoup(html, 'html.parser')
encontrei = soup.find('h1', id='hello-world')
encontrei2 = soup.find('p', {'class':'definition'})
print(encontrei.get_text())
print(encontrei2.get_text())