import mysql.connector
import pandas as pd

def limpeza2():
    #conectar ao servidor
    con = mysql.connector.connect(
        host = '170.245.15.166',
        user = 'grupo4foda',
        password = 'entra2122g4',
        database = 'entra2122g4'
        )#conexão
    cursor = con.cursor() #cursor
    #conectar ao cursor
    if con.is_connected(): #se está conectado
        db_info = con.get_server_info()
        print("Conectado ao servidor MySQL versão",db_info)

    con #conetar

    previsao = pd.read_sql_query('SELECT * FROM PREVISAO',con) #comando que será executado
    
    previsao[['CHUVA','PRECISAO']] = previsao['MM_CHUVA_PRECI'].str.split('-',expand=True)# dividindo a coluna pelo "-"
    previsao['CHUVA'] = previsao['CHUVA'].str.replace('mm','') # apagando o mm
    previsao['PRECISAO'] = previsao['PRECISAO'].str.replace('%','') # apagando a %
    previsao_final = previsao[['DATA','DIA_SEMANA','CHUVA','PRECISAO']] # selecionando colunas 
    previsao_final['PRECISAO'] = previsao_final['PRECISAO'].astype('int32') # alterando o tipo da coluna
    
    # comando sql para apagar a tabela caso ela ja exista
    cursor.execute('''
        DROP TABLE IF EXISTS PREVISAO_TRATADA;
    ''')
    # comando sql para gerar as colunas
    cursor.execute('''
        CREATE TABLE PREVISAO_TRATADA(
            PREVISAO_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
            PREVISAO_DATA DATE NOT NULL,
            PREVISAO_CHUVA INTEGER NOT NULL,
            PREVISAO_PREVISAO INTEGER NOT NULL
    );
    ''')

    # inserindo na nuvem
    sql=('INSERT INTO PREVISAO_TRATADA (PREVISAO_DATA,PREVISAO_CHUVA,PREVISAO_PREVISAO) VALUES (%s,%s,%s) ')
    for index, row in previsao_final.iterrows():
        val=(row.DATA,row.CHUVA,row.PRECISAO)    
        cursor.execute(sql,val)
    con.commit()
    print('Adição de registros completa.')
    con.close()

    #Fechar conexão
    cursor.close()
    con.close()
    print("Conexão encerrada")