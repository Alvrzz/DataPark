from predicao_clientes.src.clientes import clientes_pred
from predicao_clientes.src.database_connect import data_pred, chuva_pred
from predicao_clientes.src.funcionarios import funcionarios_pred
import mysql.connector

def PredicaoClientes():
    cnx = mysql.connector.connect(
        host = '170.245.15.166',
        user = 'grupo4foda',
        password = 'entra2122g4',
        database = 'entra2122g4'
        )

    cur = cnx.cursor()

    cur.execute('''
        DROP TABLE IF EXISTS PREDICAO_PARQUE;
    ''')

    cur.execute('''
        CREATE TABLE PREDICAO_PARQUE(
            PREDICAO_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
            PREDICAO_DATA DATE NOT NULL,
            PREDICAO_CHUVA INTEGER NOT NULL,
            PREDICAO_FUNCIONARIOS INTEGER NOT NULL,
            PREDICAO_CLIENTES INTEGER NOT NULL
        );
    ''')

    contagem_pred = 0
    passos_pred = 1

    predicao = list(zip(data_pred, chuva_pred, funcionarios_pred, clientes_pred))

    while contagem_pred < len(data_pred):
        cur.executemany('INSERT INTO PREDICAO_PARQUE (PREDICAO_DATA, PREDICAO_CHUVA, PREDICAO_FUNCIONARIOS, PREDICAO_CLIENTES) VALUES (%s, %s, %s, %s)', predicao[contagem_pred: passos_pred])
        contagem_pred += 1
        passos_pred += 1
        cnx.commit()
        print('Adição de 1 registro da PREDIÇÃO completa.')

    print('Envio dos dados completo.')

PredicaoClientes()