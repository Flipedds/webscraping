import csv
import requests
from bs4 import BeautifulSoup

from fila import Fila

# URL da página que queremos fazer scraping
url = 'https://m.imdb.com/chart/top/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Conexão: Enviar uma solicitação GET para a URL
response = requests.get(url, headers=headers)

# Verificar se a solicitação foi bem-sucedida (status 200)
if response.status_code == 200:
    # Parse a página com o BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Encontre os elementos HTML que contêm os títulos dos filmes
    titles = soup.find_all("h3", class_="ipc-title__text")

    # Encontre os elementos HTML que contêm as informações
    infos = soup.find_all("span", class_="sc-b85248f1-6 bnDqKN cli-title-metadata-item")

    fila = Fila(750)
    for info in infos:
        fila.enfileirar(info.text)

    #cria arquivo csv
    file = open('theBestFilms.csv', 'w', newline='')
    writer = csv.writer(file)
    headers = ['Titulos | Tempo de filme | classificacao']
    writer.writerow(headers)

    skip_list = [
    'You have rated',
    'More to explore',
    'Charts',
    'Top Box Office (US)',
    'Most Popular Movies',
    'Top Rated English Movies',
    'Most Popular TV Shows',
    'Top 250 TV Shows',
    'Lowest Rated Movies',
    'Most Popular Celebs',
    'Top Rated Movies by Genre',
    'Recently viewed',
    'IMDb Charts'
    ]

    # Loop pelos elementos e imprimir os títulos
    for title in titles:
        if title.text in skip_list:
           continue
        temp = []
        for i in range(3):
            temp.append(fila.primeiro())
            fila.desenfileirar()
        ano, tempo, aged = temp
        one_title = [title.text, ano, tempo, aged]

        #salvar noticia no arquivo
        file = open('theBestFilms.csv', 'a', newline='', encoding='utf-8')
        writer = csv.writer(file)
        writer.writerow(one_title)
        file.close()

else:
    print("Falha ao acessar a página:", response.status_code)
