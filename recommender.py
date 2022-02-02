import pandas as pd
from procuraFilme import procura_filme
from limpaTela import limpar
import logging

def recomendador_filmes(nome_filme):
    logging.info(f'Iniciando funcao recomendador_filmes')
    logging.info(f'Efetuando carregametno das bases.')
    column_names = ['id_usuario','id_filme','avaliacao','timestamp']
    df = pd.read_csv('Data/user_rating.data', sep='\t', names=column_names)

    filmes = pd.read_csv('Data/Movie_Id_Titles')
    filmes.head(5)
    filmes.rename(columns={
        'item_id': 'id_filme',
        'title':'nome_filme'
    }, 
    inplace = True
    )

    df = pd.merge(df,filmes, on='id_filme')
    logging.info(f'Efetuando unificação bases.')

    avaliacoes = pd.DataFrame(df.groupby('nome_filme')['avaliacao'].mean())
    logging.info(f'Criadno campo de total_avaliações.')

    avaliacoes['total_avaliacoes'] = pd.DataFrame(df.groupby('nome_filme')['avaliacao'].count())

    logging.info(f'Efetuando o pivoteamento das bases.')

    df_final = df.pivot_table(index='id_usuario',columns='nome_filme',values='avaliacao')

    
    nome_filme = procura_filme(df_final,nome_filme)

    logging.info(f'Efetuando busca pelo nome do filme.')
    filme_avaliacoes = df_final[nome_filme]
    # Toy Story (1995)
    logging.info(f'Efetuando correlacões entre filmes')
    similar_filmes = df_final.corrwith(filme_avaliacoes)
    limpar()

    correlacaot_filmes = pd.DataFrame(similar_filmes,columns=['Correlation'])
    correlacaot_filmes.dropna(inplace=True)
    correlacaot_filmes.sort_values('Correlation',ascending=False).head()
    correlacaot_filmes = correlacaot_filmes.join(avaliacoes['total_avaliacoes'])
    logging.info(f'Montando lista de sugestões de filmes.')
    sugestoes = correlacaot_filmes[correlacaot_filmes['total_avaliacoes']> 100].sort_values('Correlation',ascending=False).head(5)
    # print(sugestoes)
    print(200*'=')
    print(f' \nAqui estão algumas sugestçoes de filmes para você:\n')
    print(sugestoes)
    print(200*'=')