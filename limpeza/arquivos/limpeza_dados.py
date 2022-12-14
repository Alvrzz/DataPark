import mysql.connector
import pandas as pd
from configuracoes.local_settings import hostip, usuario, senha, databasename

def limpeza1():
    #conectar ao servidor
    con = mysql.connector.connect(
        host = hostip,
        user = usuario,
        password = senha,
        database = databasename
        )#conexão

    cursor = con.cursor() #cursor
    #conectar ao cursor
    if con.is_connected(): #se está conectado
        db_info = con.get_server_info()
        print("Conectado ao servidor MySQL versão",db_info)


    con #conetar
    # Armazenando as tabelas em variaveis
    funcionarios = pd.read_sql_query('SELECT * FROM FUNCIONARIOS',con) #comando que será executado
    
    clima = pd.read_sql_query('SELECT * FROM CLIMA',con) #comando que será executado

    clientes = pd.read_sql_query('SELECT * FROM CLIENTES',con) #comando que será executado


    # limpeza: 

    clientes = clientes.groupby("CLIENTE_DATA",as_index=False).size() #ordenando por data
    funcionarios = funcionarios.groupby("FUNCIONARIO_DATA",as_index=False).size() # ordenando por data
    t_clientes = clientes.rename(columns={'size': 'Clientes'}) #renomeando a coluna
    t_funcionarios = funcionarios.rename(columns={'size': 'Funcionarios'}) #renomeando a coluna  
    t_funcionarios = clima.join(t_funcionarios) #inserindo um df em outro
    tabela_geral = pd.merge(t_clientes, t_funcionarios, left_on="CLIENTE_DATA", right_on="FUNCIONARIO_DATA", how='right') # parte direita de um df
    tabela_geral = tabela_geral.rename(columns={'CLIMA_CHUVA_MM': 'Chuva_mm'}) #renomeando a coluna
    tabela_geral = tabela_geral[['FUNCIONARIO_DATA','Clientes','Funcionarios','Chuva_mm']] # selecionando colunas especificas
    tabela_geral = tabela_geral.rename(columns={'FUNCIONARIO_DATA': 'Data'}) # renomeando a coluna

    enviar = tabela_geral # armazenando a tabela em outra variavel para caso ocorra um erro a variavel antiga não seja alterada

    # comando sql para apagar a tabela caso ela ja exista
    cursor.execute('''
        DROP TABLE IF EXISTS TABELA_GERAL;
    ''')
    # comando sql para criar a tabela e suas colunas 
    cursor.execute('''
        CREATE TABLE TABELA_GERAL(
            TABELA_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
            TABELA_DATA DATE NOT NULL,
            TABELA_CLIENTES INTEGER NOT NULL,
            TABELA_FUNCIONARIOS INTEGER NOT NULL,
            TABELA_CHUVA INTEGER NOT NULL
    );
    ''')

    # inserindo na nuvem
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

