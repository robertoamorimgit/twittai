import os

def ler_titulos():
    if not os.path.exists('titulos.txt'):
        return set()
    
    with open('titulos.txt', 'r') as file:
        return set(file.read().splitlines())

def armazenar_titulo(titulo):
    with open('titulos.txt', 'a') as file:
        file.write(titulo + '\n')

def filtrar_noticias(novas_noticias):
    titulos_existentes = ler_titulos()
    noticias_filtradas = []

    for noticia in novas_noticias:
        if noticia['title'] not in titulos_existentes:
            noticias_filtradas.append(noticia)
            armazenar_titulo(noticia['title'])
    
    return noticias_filtradas
