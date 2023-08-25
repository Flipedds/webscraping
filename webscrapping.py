import csv
import requests
from bs4 import BeautifulSoup
from fila import Fila
from consts import URL, HEADERS, SKIP_LIST

# Conexão: Enviar uma solicitação GET para a URL
response = requests.get(URL, headers=HEADERS)

# Verificar se a solicitação foi bem-sucedida (status 200)
if response.status_code == 200:
    # Parse a página com o BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Encontre os elementos HTML que contêm os títulos dos filmes
    titles = soup.find_all("h3", class_="ipc-title__text")

    # Encontre os elementos HTML que contêm as informações dos filmes
    infos = soup.find_all("span", class_="sc-b85248f1-6 bnDqKN cli-title-metadata-item")

    fila = Fila(750)
    for info in infos: # adiciona cada informação em uma fila
        fila.enfileirar(info.text)

    #cria arquivo csv
    file = open('theBestFilms.csv', 'w', newline='')
    writer = csv.writer(file)
    headers = ['Titulos | Ano do filme | Tempo de filme | classificacao']
    writer.writerow(headers)

    # Loop pelos elementos e imprimir os títulos
    for title in titles:
        if title.text in SKIP_LIST: # se o título for algum da lista pula para o próximo sem adicionar
           continue
        temp = [] # lista temporária que vai receber os itens vindo da fila
        for i in range(3):
            temp.append(fila.primeiro())
            fila.desenfileirar()
        ano, tempo, aged = temp # desestruturação da lista
        one_title = [title.text, ano, tempo, aged]

        #salvar tudo no arquivo
        file = open('theBestFilms.csv', 'a', newline='', encoding='utf-8')
        writer = csv.writer(file)
        writer.writerow(one_title)
        file.close()

else:
    print("Falha ao acessar a página:", response.status_code)
