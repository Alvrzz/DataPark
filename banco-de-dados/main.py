import sqlite3
import pandas as pd 



cnx = sqlite3.connect('dbparque.sqlite3')
cur = cnx.cursor()




cur.execute("""
    DROP TABLE IF EXISTS CIDADES; 
""")

cur.execute("""
    DROP TABLE IF EXISTS CLIMA; 
""")

cur.execute("""    
    CREATE TABLE CLIMA (
            CLIMA_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            CLIMA_DATA TEXT NOT NULL,
            CLIMA_CHUVAMM INTEGER,
            CLIMA_TEMPMIN FLOAT NOT NULL,
            CLIMA_TEMPMAX FLOAT NOT NULL
    );
""")

cur.execute("""
    DROP TABLE IF EXISTS CLIENTES; 
""")

cur.execute("""
    CREATE TABLE CLIENTES(
        CLIENTE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CLIENTE_DATA TEXT NOT NULL,
        CLIENTE_NOME TEXT NOT NULL, 
        CLIENTE_CPF TEXT NOT NULL,
        CLIENTE_IDADE INTEGER NOT NULL,
        CLIENTE_UF TEXT NOT NULL,
        CLIENTE_CIDADE TEXT NOT NULL
    );
""")

cur.execute("""
    DROP TABLE IF EXISTS FUNCIONARIOS; 
""")

cur.execute("""
    CREATE TABLE FUNCIONARIOS(
        FUNCIONARIO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        FUNCIONARIO_DATA TEXT NOT NULL,
        FUNCIONARIO_NOME TEXT NOT NULL, 
        FUNCIONARIO_ATRACOES_ID INTEGER NOT NULL
        );
""")

cur.execute("""
    DROP TABLE IF EXISTS ATRACOES; 
""")

cur.execute("""    
    CREATE TABLE ATRACOES (
            ATRACAO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ATRACAO_NOME TEXT NOT NULL
    );
""")


#Tabela Funcionarios
url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTq6H-BIadfoWHZMG6-1s3qu2B5SGtMEBlLxe9lJtAkKlhKFI4AXznlPutq_DHZOQDFU5XITuClfhU4/pub?gid=529254615&single=true&output=csv'
colunas = list(['id','data','nome','atracao_id'])
df = pd.read_csv(url_or_file, index_col=0, header=0, usecols=colunas)
# print(df)
sql=("INSERT INTO FUNCIONARIOS (FUNCIONARIO_DATA, FUNCIONARIO_NOME, FUNCIONARIO_ATRACOES_ID) VALUES (?,?,?) ")
for index, row in df.iterrows():
    val=(row.data, row.nome, row.atracao_id)    
    cur.execute(sql,val)
cnx.commit()

#Tabela Atracoes
url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSsZFUGTJc-4IJpbjFdUSbLm3Hwr4ORxTjipytWCsehG-KbuRJJ3F5oL2jcUz0Sb8XAZkPEFXMv5iM3/pub?gid=1056840368&single=true&output=csv'
colunas = list(['id','nome'])
df = pd.read_csv(url_or_file, index_col=0, header=0, usecols=colunas)
# print(df)
# sql=("INSERT INTO ATRACOES (ATRACAO_NOME) VALUES (?) ")
# for index, row in df.iterrows():
#     val=(row.nome)    
#     cur.execute(sql,val)
# cnx.commit()


#Tabela Clima
url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRLpVtG3J9mmBRMVFoxHtIM3yG9pGh4vd8ynUr72Fi28CWt6bQhHaWhZNio7VsrDNoBB974e0LQiOYC/pub?gid=504172621&single=true&output=csv'
colunas = list(['Id','Data', 'Chuva', 'Tempmin', 'Tempmax'])
df = pd.read_csv(url_or_file, index_col=0, header=0, usecols=colunas)
# print(df)
sql=("INSERT INTO CLIMA (CLIMA_DATA, CLIMA_CHUVAMM, CLIMA_TEMPMIN, CLIMA_TEMPMAX) VALUES (?,?,?,?) ")
for index, row in df.iterrows():
    val=(row.Data, row.Chuva, row.Tempmin, row.Tempmax)    
    cur.execute(sql,val)
cnx.commit()



cur.close



