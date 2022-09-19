import mysql.connector
import pandas as pd

def tratamento1():
    #conectar ao servidor
    con = mysql.connector.connect(host='3.89.36.150',database='e2122g4',user='e2122g4',password='e2122g4@16@ago')#conexão

    cursor = con.cursor() #cursor
    #conectar ao cursor
    if con.is_connected(): #se está conectado
        db_info = con.get_server_info()
        print("Conectado ao servidor MySQL versão",db_info)


    con #conetar

    funcionarios = pd.read_sql_query('SELECT * FROM FUNCIONARIOS',con) #comando que será executado
    clima = pd.read_sql_query('SELECT * FROM CLIMA',con) #comando que será executado





    clientes = pd.read_sql_query('SELECT * FROM CLIENTES',con) #comando que será executado





    clientes = pd.read_sql_query('SELECT * FROM CLIENTES',con) #comando que será executado


    # # Tratamento: 


    clientes = clientes.groupby("CLIENTE_DATA",as_index=False).size()





    funcionarios = funcionarios.groupby("FUNCIONARIO_DATA",as_index=False).size()





    t_clientes = clientes.rename(columns={'size': 'Clientes'})




    t_funcionarios = funcionarios.rename(columns={'size': 'Funcionarios'})



    t_funcionarios = clima.join(t_funcionarios)




    tabela_geral = pd.merge(t_clientes, t_funcionarios, left_on="CLIENTE_DATA", right_on="FUNCIONARIO_DATA", how='right')


    tabela_geral = tabela_geral.rename(columns={'CLIMA_CHUVA_MM': 'Chuva_mm'})



    tabela_geral = tabela_geral[['FUNCIONARIO_DATA','Clientes','Funcionarios','Chuva_mm']]




    tabela_geral = tabela_geral.rename(columns={'FUNCIONARIO_DATA': 'Data'})




    enviar = tabela_geral


    cursor.execute('''
        DROP TABLE IF EXISTS TABELA_GERAL;
    ''')

    cursor.execute('''
        CREATE TABLE TABELA_GERAL(
            TABELA_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
            TABELA_DATA DATE NOT NULL,
            TABELA_CLIENTES INTEGER NOT NULL,
            TABELA_FUNCIONARIOS INTEGER NOT NULL,
            TABELA_CHUVA INTEGER NOT NULL
    );
    ''')


    sql=('INSERT INTO TABELA_GERAL (TABELA_DATA,TABELA_CLIENTES,TABELA_FUNCIONARIOS,TABELA_CHUVA) VALUES (%s,%s,%s,%s) ')
    for index, row in enviar.iterrows():
        val=(row.Data,row.Clientes,row.Funcionarios,row.Chuva_mm)    
        cursor.execute(sql,val)
    con.commit()
    print('Adição de registros completa.')
    con.close()



    #Fechar conexão
    cursor.close()
    con.close()
    print("Conexão encerrada")

