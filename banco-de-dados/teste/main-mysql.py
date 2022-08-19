

import mysql.connector
import pandas as pd 
import random


cnx = mysql.connector.connect(
    host = '3.89.36.150',
    user = 'e2122g4',
    password = 'e2122g4@16@ago',
    database = 'e2122g4'
    )

cur = cnx.cursor()

cur.execute("""
    DROP TABLE IF EXISTS CIDADES; 
""")

cur.execute("""    
    CREATE TABLE CIDADES (
            CIDADE_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
            CIDADE_UF TEXT NOT NULL,
            CIDADE_NOME TEXT NOT NULL
    );
""")

cur.execute("""
    DROP TABLE IF EXISTS PESSOAS; 
""")

cur.execute("""
    CREATE TABLE PESSOAS(
        PESSOA_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
        PESSOA_NOME TEXT NOT NULL,
        PESSOA_IDADE INTEGER, 
        PESSOA_CIDADE_ID INTEGER NOT NULL
    );
""")



#  Tabela de Cidades
url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSp3N0iSajaKoFaRiiTOV1Qxm1Y6-_B1IKJsKaqjiBhJbNIrjER4Kr2YtDHn8xNsFvWhQiGBK-Q5MQN/pub?gid=0&single=true&output=csv'
colunas = list(['id','UF','Município'])
cont = pd.read_csv(
    url_or_file, 
    index_col=0, header=0,   
    usecols=colunas
                )

tamanho=5
cont = (len(cont))
print(cont)
inicio = 1

while inicio < cont:

    df = pd.read_csv(
        url_or_file, 
        index_col=0, header=0,
#        skiprows=(inicio),     
        nrows=tamanho, 
        usecols=colunas)
    print(inicio)
inicio = inicio + tamanho


    # numero_cidades = list((df.shape))[0]

    # sql=("INSERT INTO CIDADES (CIDADE_UF,CIDADE_NOME) VALUES (%s, %s) ")
    # for index, row in df.iterrows():
    #     val=(row.UF, row.Município)    
    #     cur.execute(sql,val)

    # cnx.commit()




# Tabela de Pessoas

# url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQrw2IJT8L_iuyYyZRehzDK89pNRRQUEVvUl1KxEJ8U182AEkUMIyWtGtQf3SHG8rxsEoni_-cqr4yo/pub?gid=945554847&single=true&output=csv'

# colunas = list(['id','first_name'])
# df = pd.read_csv(url_or_file, index_col=0, header=0, nrows=tamanho, usecols=colunas)
# a = list((df.shape))[0] 


# sql=("INSERT INTO PESSOAS (PESSOA_NOME,PESSOA_IDADE,PESSOA_CIDADE_ID) VALUES (%s, %s, %s) ")
# for index,row in df.iterrows():
#     nome = row.first_name
#     idade = random.randrange(0,120)
#     cidade_id = random.randrange(1,numero_cidades)          
#     # print(nome,idade,cidade_id)
#     val=(nome,idade,cidade_id)
#     cur.execute(sql,val)
# cnx.commit()
cur.close




 










