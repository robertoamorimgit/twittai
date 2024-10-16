from .beautifulsoup_scrapy import coletar_braziljournal, coletar_revistaoeste

def coletar_noticias():
    noticias = []
    
    # Coletar do Brazil Journal
    noticias += coletar_braziljournal()
    
    # Coletar da Revista Oeste
    noticias += coletar_revistaoeste()
    
    return noticias
