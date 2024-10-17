from coletor.beautifulsoup_scrapy import coletar_todas_as_noticias
from processador.processamento import filtrar_noticias, processar_noticias

def main():
    novas_noticias = coletar_todas_as_noticias()
    noticias_filtradas = filtrar_noticias(novas_noticias)
    noticias_processadas = processar_noticias(noticias_filtradas)

    salvar_noticias(noticias_processadas)

def salvar_noticias(noticias):
    with open('/app/dados/noticias_processadas.txt', 'a') as file:
        for noticia in noticias:
            file.write(f"{noticia['title']}\n")

if __name__ == '__main__':
    main()
