import requests
from bs4 import BeautifulSoup

def coletar_revistaoeste():
    url = 'https://revistaoeste.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify())  # Adicione isso para inspecionar a estrutura
    articles = soup.find_all('article')
    noticias = []
    for article in articles:
        title = article.h2.text.strip() if article.h2 else 'No Title'
        noticias.append({'title': title, 'source': 'Revista Oeste'})
    return noticias
