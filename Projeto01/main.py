from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://alura-site-scraping.herokuapp.com/hello-world.php'

# Vamos passar o url pela função que irá abrir todos os
# dados que se encontram na url
response = urlopen(url)
# Vamos ler esse dados em html
html = response.read()
# Vamos criar um object tipo soup para ficar mais légivel
# para nós e para a máquina também.
soup = BeautifulSoup(html, 'html.parser')
# Através de Algumas funcionabilidades nós podemos obeter
# resultados filtrados.
dado_test = soup.find('h1', id='hello-world')
# Com apenas o texto
dado_test2 = soup.find('h1', id='hello-world').get_text()
# Vamos agora pegar os dados da subscrição
dado_test3 = soup.find('p')
# Apenas o texto
dado_test4 = soup.find('p').get_text()
# Filtrando ainda mais
dado_test5 = soup.find('p', {'class': 'definition'})
# Apenas o texto
dado_test6 = soup.find('p', {'class': 'definition'}).get_text()

print('>>>>>>>>Inicio - Testes<<<<<<<<<')
print('O html')
print(html)
print('O soup\n\n')
print(soup)
print('\n\nH1')
print(dado_test)
print('h1 doidera')
print(dado_test2)
print('subtítulo')
print(dado_test3)
print(dado_test4)
print(dado_test5)
print(dado_test6)
print('>>>>>>>>>>>Fim - Testes<<<<<<<<<')