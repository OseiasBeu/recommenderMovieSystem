from recommender import recomendador_filmes
from limpaTela import limpar
import logging
LOG_FILENAME = 'logs/logs.log'
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(handlers=[logging.FileHandler(filename=LOG_FILENAME, encoding='utf-8', mode='a+')],format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

key = True
while key:
    try:
        limpar()
        print(200*'=')
        print(200*'=')
        logging.info(100*'=')
        logging.info(f'==========| Iniciando Sistema de Recomendação|==========')
        print(''' BEM VINDO AO IDICADOR DE FILMES!''')
        print(200*'-')
        nome_filme = input('Digite o nome do filme que está procurando: ')
        limpar()
        print(200*'-')
        recomendador_filmes(nome_filme)
        print(200*'-')
        continuar = input('Desejar mais recomendações?[S/N]')
        if continuar == 'N':
            limpar()
            logging.info(f'==========| Finalzando Sistema de Recomendação|==========')
            logging.info(100*'=')
            key = False
    except Exception as e:
        logMessage = f'Status de erro: {e}'
        logging.error(f'Um erro inesperado aconteceu:')
        logging.error(logMessage)
        logging.error(100*'X')





