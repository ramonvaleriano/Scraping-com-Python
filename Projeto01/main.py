from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://alura-site-scraping.herokuapp.com/hello-world.php'

reponse = urlopen(url)
html = reponse.read()

soup = BeautifulSoup(html, "html.parser")
print(soup)
h1 = soup.find('h1')
print(h1)
text_h1 = soup.find('h1').get_text()
print(text_h1)




