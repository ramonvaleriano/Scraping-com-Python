from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://alura-site-scraping.herokuapp.com/hello-world.php'

response = urlopen(url)
html = response.read()
print(html)

soup = BeautifulSoup(html, 'html.parser')
data_test = soup.find('h1', id='hello-world')
data_test_text = soup.find('h1', id='hello-world').get_text()
data_test_class = soup.find('p', {'class':'definition'}).get_text()
print(data_test)
print(data_test_text)
print(data_test_class)