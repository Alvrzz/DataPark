import mysql.connector


cnx = mysql.connector.connect(
    host = '170.245.15.166',
    user = 'grupo4foda',
    password = 'entra2122g4',
    database = 'entra2122g4'
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