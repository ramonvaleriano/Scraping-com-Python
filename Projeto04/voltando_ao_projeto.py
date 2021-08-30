from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


def tratando_html(html):

    return html.decode('utf-8')



url = 'https://alura-site-scraping.herokuapp.com/index.php'

headres = {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}

request = Request(url, headers=headres)

response = urlopen(request)
html = response.read()

html = tratando_html(html)

soup = BeautifulSoup(html, 'html.parser')
print('Apenas o Soup, sem qualquer Filtro.')
print(soup)
print('\n\n')
print('Passando agora Titulo')
soup_head_title = soup.html.head.title
print(soup_head_title)
print(soup_head_title.get_text())
print('\n\n')
print('Outra forma de acessar o titulo')
soup_title = soup.title
print(soup_title)
print(soup_title.get_text())
print('Acessando a Div')
soup_div = soup.div
print(soup_div)
print('\n\n')
print('Tentando acessa um conteudo interno')
soup_div_h5 = soup.div.div.div.div.h5
print(soup_div_h5)
print(soup_div_h5.get_text())