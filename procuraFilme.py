from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import logging

def procura_filme(df,nome_filme):
    logging.info(f'Iniciando função procura_filmes')
    dict_nomes = {}
    contador = 1
    logging.info(f'Efetuando busca por nomes similares.')
    nomes_similares = process.extract(nome_filme, df.columns, scorer=fuzz.partial_token_sort_ratio, limit=5)

    for item in nomes_similares:
        dict_nomes[contador] = item[0]
        contador += 1
    print(200*'-')
    print('Quais destas opções você quiz dizer?')
    for k,v in dict_nomes.items():
        print(f'''{k}) {v}''')
    print(200*'-')
    numero_filme_escolhido = int(input('Digite o número do filme escolhido:'))
    return dict_nomes[numero_filme_escolhido]