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

    # se os títulos e as informações existirem executa
    if titles and infos:
        try:
            fila = Fila(750) # a raspagem retorna 750 informações do site, (3 para cada um dos 250 títulos)
            for info in infos: # adiciona cada informação em uma fila
                fila.enfileirar(info.text)

            #cria arquivo csv
            file = open('theBestFilms.csv', 'w', newline='', encoding='utf-8')
            writer = csv.writer(file)
            headers = ['Título', 'Ano do filme', 'Tempo de filme', 'classificação']
            writer.writerow(headers)

            # Loop pelos elementos / organizar para salvar no arquivo
            for title in titles:
                if title.text in SKIP_LIST: # se o título for algum da lista pula para o próximo sem adicionar
                    continue
                temp = [] # lista temporária que vai receber os itens vindo da fila
                for i in range(3):
                    temp.append(fila.primeiro()) # adiciona a temp o primeiro da fila
                    fila.desenfileirar() # desenfileira para o ponteiro apontar para o próximo
                ano, tempo, aged = temp # desestruturação da lista
                one_title = [title.text, ano, tempo, aged]

                #salvar tudo no arquivo
                file = open('theBestFilms.csv', 'a', newline='', encoding='utf-8')
                writer = csv.writer(file)
                writer.writerow(one_title)
                file.close()
        except:
            print("Falha ao encontrar os elementos")
            
else:
    print("Falha ao acessar a página:", response.status_code)
