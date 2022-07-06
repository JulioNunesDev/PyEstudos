import requests
import json

def search(titulo):
    try:
        requisicao = requests.get('http://www.omdbapi.com/?apikey=935e0f8b&t=' + titulo)
        response = json.loads(requisicao.text)
        return response
    except Exception as err:
        print('Nao foi possivel a requisição', err)
        return None


def showMovies(filme):
    print('Titulo:', filme['Title'])
    print('Gêneros:', filme['Genre'])
    print('Ano:', filme['Year'])
    print('Diretor:', filme['Director'])
    print('Atores:', filme['Actors'])
    print('Prêmios:', filme['Awards'])
    print('Poster:', filme['Poster'])
    print('IMDB:', filme['imdbRating'])
    print('')

sair = False
while not sair:
    op = input('Digite o nome de algum filme ou "SAIR" para fechar:>> ')
    if op == 'SAIR':
        sair = True
        print('Saindo...')
    else:
        filme = search(op)
        if filme['Response'] == 'False':
            print('Filme nao encontrado', filme['Error'])
        else:
            showMovies(filme)
