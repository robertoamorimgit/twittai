def salvar_processamento(noticias):
    with open('/app/dados/noticias_processadas.txt', 'a') as file:
        for noticia in noticias:
            file.write(f"{noticia['title']}\n")

def filtrar_noticias(novas_noticias):
    titulos_existentes = ler_titulos()
    noticias_filtradas = []

    for noticia in novas_noticias:
        if noticia['title'] not in titulos_existentes:
            noticias_filtradas.append(noticia)
            armazenar_titulo(noticia['title'])
    
    return noticias_filtradas

def processar_noticias(noticias):
    # Seu código de processamento
    noticias_processadas = [noticia for noticia in noticias]  # Processa as notícias
    salvar_processamento(noticias_processadas)
    return noticias_processadas

def ler_titulos():
    if not os.path.exists('/app/dados/titulos.txt'):
        return set()
    
    with open('/app/dados/titulos.txt', 'r') as file:
        return set(file.read().splitlines())

def armazenar_titulo(titulo):
    with open('/app/dados/titulos.txt', 'a') as file:
        file.write(titulo + '\n')
