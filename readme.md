# Coleta de dados (web scraping) - Big Data

Instruções da atividade: 

    Escolha 1 site de sua preferência e realize web scraping com a biblioteca BeautifulSoup, formando uma base de dados (com 1 característica do site) salva em arquivo csv.

    Sugestão de problemas (diferente do exemplo abordado em sala):

    · Site IMDB

    · Preços de produtos

    · Sites de notícias

    · Meteorologia

Site escolhido:

    https://m.imdb.com/chart/top/


Dados a serem raspados:

    Títulos dos filmes, ano, tempo de exibição e classificação indicativa

Necessário para o funcionamento do código:

    Python 3.11.4 -> não testado em outras versões, pode ou não funcionar !

    pip install -r requirements.txt


Arquivos:

    webscrapping.py -> principal -> arquivo a ser executado

    fila.py -> classe que cria uma fila para inserir e mostrar informações

    consts.py -> algumas constantes importantes para o funcionamento do Script
    
    TheBestFilms.csv -> csv gerado após a raspagem dos dados
