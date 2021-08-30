from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

url = 'https://www.alura.com.br/'

headers = {
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

try:
    request = Request(url, headers=headers)
    response = urlopen(request)

    html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    print(soup)

except HTTPError as erro_http:
    print(erro_http.status, erro_http.reason)

except URLError as erro_url:
    print(erro_url.status, erro_url.reason)