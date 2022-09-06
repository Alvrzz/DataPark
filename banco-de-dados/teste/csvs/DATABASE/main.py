from CHUVA import clientes, weather
from DATA import data
from NOMES import nomes
from CPF import cpfe
from CIDADES_CONT import numcidades, cidade_id
from IDADE import idade
from DATA_TOTAL import data_mult
import mysql.connector, pandas as pd, random, sqlite3

contagem = 0
passos = 100000


# cnx = sqlite3.connect('exer200pt2.sqlite3')

cnx = mysql.connector.connect(
    host = '3.89.36.150',
    user = 'e2122g4',
    password = 'e2122g4@16@ago',
    database = 'e2122g4'
    )

cur = cnx.cursor()


# cur.execute('''
#     DROP TABLE IF EXISTS CLIENTES;
# ''')

# cur.execute('''
#     CREATE TABLE CLIENTES(
#         CLIENTE_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
#         CLIENTE_NOME TEXT,
#         CLIENTE_IDADE INTEGER,
#         CLIENTE_DATA TEXT,
#         CLIENTE_CPF TEXT,
#         CLIENTE_CIDADE_ID INTEGER
#     );
# ''')

clientes_final = list(zip(nomes, idade, data_mult, cpfe, cidade_id))
data_final = list(zip(data, weather))


df = pd.DataFrame(clientes_final)
df.to_csv('CLIENTES.csv', index=False, header=False)

df2 = pd.DataFrame(data_final)
df2.to_csv('CHUVA', index=False, header=False)
# while contagem < sum(clientes):
#     cur.executemany('INSERT INTO CLIENTES (CLIENTE_NOME, CLIENTE_IDADE, CLIENTE_DATA, CLIENTE_CPF, CLIENTE_CIDADE_ID) VALUES (%s, %s, %s, %s, %s)', values[contagem: passos])
#     contagem += 100000
#     passos += 100000
#     cnx.commit()
#     print('Adição de 100 mil registros completa.')
# cnx.close()