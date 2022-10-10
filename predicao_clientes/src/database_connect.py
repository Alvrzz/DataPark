import mysql.connector
from configuracoes.local_settings import hostip, usuario, senha, databasename


cnx = mysql.connector.connect(
    host = hostip,
    user = usuario,
    password = senha,
    database = databasename
    )

cur = cnx.cursor()

cur.execute('SELECT * FROM PREVISAO_TRATADA')

data_pred = []
chuva_pred = []
chance_chuva = []

for i in cur:
    data_pred.append(i[1].isoformat())
    chuva_pred.append(i[2])
    chance_chuva.append(i[3])