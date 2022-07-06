import re
import requests

# RAW Strings são strings cruas
requisicao = requests.get('https://loucosporcoxinha.com.br/contato')
dados = re.search('[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text)

if dados:
    print(dados)
else:
    print('Nao foi encontrado nenhum E-mail')
