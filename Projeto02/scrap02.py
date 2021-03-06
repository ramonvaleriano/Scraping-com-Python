from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

url = 'https://www.alura.com.br'

print(url)

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
}

try:
    request = Request(url=url, headers=headers)
    response = urlopen(request)
    html = response.read()
    print(html)

except HTTPError as error1:
    print(error1.status, error1.reason)

except URLError as erro2:
    print(erro2.status, erro2.reason)