from coletor.coleta import coletar_noticias
from processador.processamento import filtrar_noticias

def main():
    novas_noticias = coletar_noticias()
    noticias_filtradas = filtrar_noticias(novas_noticias)

    for noticia in noticias_filtradas:
        print(f"Fonte: {noticia['source']}, Título: {noticia['title']}")

if __name__ == '__main__':
    main()


'''rodar assim : python main.py'''