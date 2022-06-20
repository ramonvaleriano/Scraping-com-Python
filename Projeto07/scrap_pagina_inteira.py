from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve

url = 'https://alura-site-scraping.herokuapp.com/index.php'

response = urlopen(url)
html = response.read().decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')

anuncios = soup.find('div', {'id': 'container-cards'}).findAll('div', class_='well card')

cards = list()

for anuncio in anuncios:

    card = dict()

    card['value'] = anuncio.find('div', {'class': 'value-card'}).getText()
    card['value'] = " ".join(card['value'].split())

    infos = anuncio.find('div', {'class': 'body-card'}).findAll('p')

    for info in infos:
        card[info.get('class')[0].split('-')[-1]] = info.getText()

    items = anuncio.find('div', {'class': 'body-card'}).ul.findAll('li')
    items.pop(-1)

    acessorios = list()

    for item in items:
        acessorios.append(item.getText().replace('►', '').strip())

    card['items'] = acessorios.copy()

    cards.append(card)

    image = anuncio.find('div', {'class': 'image-card'}).img.get('src')

    urlretrieve(image, './arquivos_coletados/' + image.split('/')[-1])