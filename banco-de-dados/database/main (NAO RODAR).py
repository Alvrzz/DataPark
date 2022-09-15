from chuva_clientes.chuva import clientes, weather
from chuva_clientes.data import data
from chuva_clientes.nomes import nomes
from chuva_clientes.cpf import cpfe
from chuva_clientes.cidades_cont import cidade_id
from chuva_clientes.idade import idade
from chuva_clientes.data_total import data_mult
from atracoes.atracoes import atracoes, setor
from funcionarios.data_mult import data_mult_funcionarios
from funcionarios.funcionarios import funcionarios
from predicao_clientes.clientes import clientes_pred
from predicao_clientes.database_connect import data_pred, chuva_pred
from predicao_clientes.funcionarios import funcionarios_pred
import mysql.connector
import pandas as pd

# Gera 98640 ids para as atrações, para ser usado na tabela de funcionarios
atracao = [x for x in range(1, 19)]
atracao = atracao * 5480

# Variáveis para a contagem e passos dos while
contagem_clientes = 0
contagem_clima = 0
contagem_atracao = 0
contagem_funcionarios = 0
passos_clientes = 100000
passos_clima = 100
passos_atracao = 10
passos_funcionarios = 10000

# Conexão com o database
cnx = mysql.connector.connect(
    host = '3.89.36.150',
    user = 'e2122g4',
    password = 'e2122g4@16@ago',
    database = 'e2122g4'
    )

cur = cnx.cursor()

# Cria todas as tabelas do database
cur.execute('''
    DROP TABLE IF EXISTS CLIENTES;
''')

cur.execute('''
    CREATE TABLE CLIENTES(
        CLIENTE_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
        CLIENTE_NOME TEXT NOT NULL,
        CLIENTE_IDADE INTEGER NOT NULL,
        CLIENTE_DATA DATE NOT NULL,
        CLIENTE_CPF TEXT NOT NULL,
        CLIENTE_CIDADE_ID INTEGER NOT NULL
    );
''')

cur.execute('''
    DROP TABLE IF EXISTS CLIMA;
''')

cur.execute('''
    CREATE TABLE CLIMA(
        CLIMA_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
        CLIMA_DATA DATE NOT NULL,
        CLIMA_CHUVA_MM INTEGER NOT NULL
    );
''')

cur.execute('''
    DROP TABLE IF EXISTS ATRACOES;
''')

cur.execute('''
    CREATE TABLE ATRACOES(
        ATRACAO_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
        ATRACAO_NOME TEXT NOT NULL,
        ATRACAO_SETOR TEXT NOT NULL
    );
''')


cur.execute('''
    DROP TABLE IF EXISTS FUNCIONARIOS;
''')

cur.execute('''
    CREATE TABLE FUNCIONARIOS(
        FUNCIONARIO_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
        FUNCIONARIO_NOME TEXT NOT NULL,
        FUNCIONARIO_DATA DATE NOT NULL,
        FUNCIONARIO_ATRACAO_ID INTEGER NOT NULL
    );
''')

cur.execute("""
    DROP TABLE IF EXISTS CIDADES; 
""")

cur.execute("""    
    CREATE TABLE CIDADES(
            CIDADE_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
            CIDADE_UF TEXT NOT NULL,
            CIDADE_NOME TEXT NOT NULL
    );
""")


# Cria tuplas com todos os dados para enviar ao database
clientes_final = list(zip(nomes, idade, data_mult, cpfe, cidade_id))
data_final = list(zip(data, weather))
atracao_final = list(zip(atracoes, setor))
funcionarios = list(zip(funcionarios, data_mult_funcionarios, atracao))

# Envia todas tuplas para o database na nuvem
while contagem_clientes < sum(clientes):
    cur.executemany('INSERT INTO CLIENTES (CLIENTE_NOME, CLIENTE_IDADE, CLIENTE_DATA, CLIENTE_CPF, CLIENTE_CIDADE_ID) VALUES (%s, %s, %s, %s, %s)', clientes_final[contagem_clientes: passos_clientes])
    contagem_clientes += 100000
    passos_clientes += 100000
    cnx.commit()
    print('Adição de 100 mil registros de CLIENTES completa.')

while contagem_clima < len(data_final):
    cur.executemany('INSERT INTO CLIMA (CLIMA_DATA, CLIMA_CHUVA_MM) VALUES (%s, %s)', data_final[contagem_clima: passos_clima])
    contagem_clima += 100
    passos_clima += 100
    cnx.commit()
    print('Adição de 100 registros de CHUVA completa.')

while contagem_atracao < len(atracoes):
    cur.executemany('INSERT INTO ATRACOES (ATRACAO_NOME, ATRACAO_SETOR) VALUES (%s, %s)', atracao_final[contagem_atracao: passos_atracao])
    contagem_atracao += 10
    passos_atracao += 10
    cnx.commit()
    print('Adição de 10 registros de ATRACOES completa.')

while contagem_funcionarios < len(data_mult_funcionarios):
    cur.executemany('INSERT INTO FUNCIONARIOS (FUNCIONARIO_NOME, FUNCIONARIO_DATA, FUNCIONARIO_ATRACAO_ID) VALUES (%s, %s, %s)', funcionarios[contagem_funcionarios: passos_funcionarios])
    contagem_funcionarios += 10000
    passos_funcionarios += 10000
    cnx.commit()
    print('Adição de 10000 registros de FUNCIONARIOS completa.')

cidades = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSqpxiXuROqjtAI24wP7WSLvg6YlwOHKfQASvXZ3I-zRmxCW6Q2oDx_IG8uT0rdIBUxomunDyURxW-G/pub?gid=385229407&single=true&output=csv'
colunas = list(['ID','UF', 'Município'])
df = pd.read_csv(cidades, index_col=0, header=0, usecols=colunas)
sql=("INSERT INTO CIDADES (CIDADE_UF, CIDADE_NOME) VALUES (%s, %s) ")
for index, row in df.iterrows():
    val=(row.UF, row.Município)
    cur.execute(sql,val)
cnx.commit()
print('Adição da tabela de CIDADES completa.')
    
cnx.close()