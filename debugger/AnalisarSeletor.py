import requests
from bs4 import BeautifulSoup

def coletar_revistaoeste():
    url = 'https://revistaoeste.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.select('article')  # Use select() se find_all() não funcionar
    noticias = []
    for article in articles:
        title = article.h2.text.strip() if article.h2 else 'No Title'
        noticias.append({'title': title, 'source': 'Revista Oeste'})
    return noticias
