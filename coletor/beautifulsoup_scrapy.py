import requests
from bs4 import BeautifulSoup

def coletar_braziljournal():
    url = 'https://braziljournal.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')
    
    noticias = []
    for article in articles:
        title = article.h2.text.strip() if article.h2 else 'No Title'
        noticias.append({'title': title, 'source': 'Brazil Journal'})
    
    return noticias

def coletar_revistaoeste():
    url = 'https://revistaoeste.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.select('main section div article a')
    
    noticias = []
    for article in articles:
        title = article.get('title', 'No Title')
        noticias.append({'title': title, 'source': 'Revista Oeste'})
    
    return noticias
