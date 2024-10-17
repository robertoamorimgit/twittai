import subprocess
import sys
import os
import requests
from bs4 import BeautifulSoup

# Adicione o diretório raiz ao caminho de importação
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def executar_teste(teste_func):
    try:
        teste_func()
    except Exception as e:
        print(f"Erro ao executar {teste_func.__name__}: {e}")

def teste_resposta_site():
    from coletor.beautifulsoup_scrapy import coletar_revistaoeste
    response = requests.get('https://revistaoeste.com')
    print(f"Status Code: {response.status_code}")

def teste_estrutura_html():
    from coletor.beautifulsoup_scrapy import coletar_revistaoeste
    response = requests.get('https://revistaoeste.com')
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify())

def teste_seletor():
    from coletor.beautifulsoup_scrapy import coletar_revistaoeste
    noticias = coletar_revistaoeste()
    for noticia in noticias:
        print(f"Fonte: {noticia['source']}, Título: {noticia['title']}")

if __name__ == '__main__':
    executar_teste(teste_resposta_site)
    executar_teste(teste_estrutura_html)
    executar_teste(teste_seletor)
