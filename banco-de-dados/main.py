import sqlite3
import pandas as pd 



cnx = sqlite3.connect('dbparque.sqlite3')
cur = cnx.cursor()




cur.execute("""
    DROP TABLE IF EXISTS CIDADES; 
""")

# cur.execute("""
#     DROP TABLE IF EXISTS CLIMA; 
# """)

# cur.execute("""    
#     CREATE TABLE CLIMA (
#             CLIMA_ID INTEGER PRIMARY KEY AUTOINCREMENT,
#             CLIMA_DATA TEXT NOT NULL,
#             CLIMA_CHUVAMM INTEGER,
#             CLIMA_TEMPMIN FLOAT NOT NULL,
#             CLIMA_TEMPMAX FLOAT NOT NULL
#     );
# """)

# cur.execute("""
#     DROP TABLE IF EXISTS CLIENTES; 
# """)

# cur.execute("""
#     CREATE TABLE CLIENTES(
#         CLIENTE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         CLIENTE_DATA TEXT NOT NULL,
#         CLIENTE_NOME TEXT NOT NULL, 
#         CLIENTE_CPF TEXT NOT NULL,
#         CLIENTE_IDADE INTEGER NOT NULL,
#         CLIENTE_UF TEXT NOT NULL,
#         CLIENTE_CIDADE TEXT NOT NULL
#     );
# """)

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

# cur.execute("""
#     DROP TABLE IF EXISTS ATRACOES; 
# """)

# cur.execute("""    
#     CREATE TABLE ATRACOES (
#             ATRACAO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
#             ATRACAO_NOME TEXT NOT NULL
#     );
# """)



url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vT2xhSxL8ghDzNmVcaBec3H3galcT6rtxFaPqufI9K2wRQ-in0BW8hE7XqWW2hI5nRaf6bGLhP7HUUk/pub?gid=0&single=true&output=csv'
colunas = list(['id','data','nome','atracao_id'])
df = pd.read_csv(url_or_file, index_col=0, header=0, usecols=colunas)

# print(df)


sql=("INSERT INTO FUNCIONARIOS (FUNCIONARIO_DATA, FUNCIONARIO_NOME, FUNCIONARIO_ATRACOES_ID) VALUES (?,?,?) ")
for index, row in df.iterrows():
    val=(row.data, row.nome, row.atracao_id)    
    cur.execute(sql,val)

cnx.commit()

cur.close



#Cidades
#https://docs.google.com/spreadsheets/d/e/2PACX-1vSNCRSky5LXh-rcR9TpHd26yNotvIgeGcGqmgZTEin2kUP9RjKhVAIRu4DfUZstqgRrkZXXapzpG7aw/pub?output=csv

#Clima
# https://docs.google.com/spreadsheets/d/e/2PACX-1vQl72SaiyWVOyzX55ofSzEJOF6F8M3gYQ3_z87f3HqY0650jlcjUK5M7wRxjwkzL8-vL5bRjLa8M55y/pub?output=csv       

#Funcionarios
#https://docs.google.com/spreadsheets/d/e/2PACX-1vSKb39CfrYvHZfTgmt63ZhPNA3L0Bsa6d8pHXF9veAwd4_Sz_3hfeOIFv2Is5DDKmOpkINZQqfpqXtt/pub?output=csv

#Clientes
#https://docs.google.com/spreadsheets/d/e/2PACX-1vToO64gKQo1Je4RNwtJW-f7H6QThRtjW2IwaXeepMkVlBV2kCouHCGykVDe54Dnb86ZPXVLTN3SzHFQ/pub?output=csv




