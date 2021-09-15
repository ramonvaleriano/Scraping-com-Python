from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://alura-site-scraping.herokuapp.com/index.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}
request = Request(url, headers=headers)

response = urlopen(request)
html = response.read()
html = html.decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')
soup_estilizado = soup.prettify()
print(soup_estilizado)