import mysql.connector


cnx = mysql.connector.connect(
    host = '3.89.36.150',
    user = 'e2122g4',
    password = 'e2122g4@16@ago',
    database = 'e2122g4'
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