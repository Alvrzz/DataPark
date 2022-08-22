import mysql.connector, pandas as pd, random,


c

# cnx = mysql.connector.connect(
#     host = '3.89.36.150',
#     user = 'e2122g1',
#     password = 'e2122g1@16@ago',
#     database = 'e2122g1'
#     )

cur = cnx.cursor()

# def tamanhotabela(df):
#     return(len(df))

# def readcsvcid(tabela):
#     tabela = ''
#     colunas = list(['ID', 'UF', 'Município'])
#     df = pd.read_csv(tabela, index_col=0, header=0, skiprows=(inicio, tamanhotabela(df), tamanho), nrows=tamanho, usecols=colunas)

# def tamtabela(tabela):
#     df1 = pd.read_csv(tabela)
#     tam = len(df1)
#     return tam
    
# def lertabela(tabela):
#     colunas = list(['ID', 'UF', 'Município'])
#     df = pd.read_csv(tabela,  index_col=0, header=0, nrows=tamanho, usecols=colunas)
#     return df

contagem = 0
inicio = 1
# passos = 10
# sair = False

cur.execute('''
    DROP TABLE IF EXISTS CIDADES;
''')

cur.execute('''
    CREATE TABLE CIDADES(
        CIDADE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CIDADE_NOME TEXT,
        CIDADE_UF TEXT
    );
''')


tabela = ('https://docs.google.com/spreadsheets/d/e/2PACX-1vSGBot2EFAMNJRdwUVK3ou7lC0uQcZE3X9NqUaVJmgd778ZVSJAAVljtZPG3eHEseo2pZQ4HKITGWZ1/pub?output=csv')
lines = pd.read_csv(tabela, index_col=0, header=0)
lines = len(lines)
print(lines)
colunas = list(['ID', 'UF', 'Municipio'])
while contagem != lines:
    # df = pd.read_csv(tabela, index_col=0, header=0, nrows = 10, usecols = colunas)
    df = pd.read_csv(tabela, index_col=0, header=0, nrows = 10, skiprows=[x for x in range(inicio, inicio + contagem)], usecols = colunas)



    # passos += 10
    contagem += 10
    # print(inicio)
    # # print(passos)
    # print(contagem)

    sql = ('INSERT INTO CIDADES (CIDADE_UF, CIDADE_NOME) VALUES (?, ?)')
    for index, row in df.iterrows():

        val = (row.UF, row.Municipio)
        cur.execute(sql,val)

    cnx.commit()
cnx.close()

# tabela = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRcfN-GUulEPs47D1rlNvxLO2tkuP-1hkx6e6p6KSIOyBGNgHb3qgW2M45QFiHwJXrNVH5_3DnLsPJX/pub?gid=931200727&single=true&output=csv'
# colunas = list(['ID', 'first_name'])
# df = pd.read_csv(tabela, index_col=0, header=0, nrows=tamanho, usecols=colunas)
# numpessoas = list((df.shape))[0]

# cur.execute('''
#     DROP TABLE IF EXISTS PESSOAS;
# ''')

# cur.execute('''
#     CREATE TABLE PESSOAS(
#         PESSOA_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
#         PESSOA_NOME TEXT,
#         PESSOA_IDADE INTEGER,
#         PESSOA_CIDADE_ID INTEGER
#     );
# ''')


# sql = ('INSERT INTO PESSOAS (PESSOA_NOME, PESSOA_IDADE, PESSOA_CIDADE_ID) VALUES (?, ?, ?)')
# for index, row in df.iterrows():
#     nome = row.first_name
#     idade = random.randrange(0, 110)
#     cidade_id = random.randrange(1, tamanhotabela_cidades)
#     val = (nome, idade, cidade_id)
#     cur.execute(sql, val)

# cnx.commit()
cur.close