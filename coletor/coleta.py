from .beautifulsoup_scrapy import coletar_todas_as_noticias

def salvar_noticias(noticias):
    with open('/app/dados/noticias_coletadas.txt', 'a') as file:
        for noticia in noticias:
            file.write(f"{noticia['title']}\n")

def coletar_noticias():
    noticias = coletar_todas_as_noticias()
    salvar_noticias(noticias)
    return noticias
