import random
import pandas as pd
import csv



tabela = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQ5dC_VioVL1uIkhoJfEqFIFXDktzzlp5292JXxM-hI051_9HOmFXID5wJa9cdYJO2VnWB4u2DQ4geC/pub?gid=240899622&single=true&output=csv'
df = pd.read_csv(tabela, index_col=0, header=0, usecols=['Id', 'TP'])
data = df['TP'].tolist()

# with open('feriados.csv') as df:
#     reader = csv.reader(df)
#     for row in reader:
#         print(row[1])

weather = []
clientes = []
loop = 0
clientes_normal = 600
feriado = 0
clientes_final = 0
while loop < 1096:
    if data[loop] == 'Sim':
        feriado = 1
    else:
        feriado = 0

    aleatchuva = random.randint(0, 1)
    if aleatchuva == 1:
        chuva = random.randint(0, 30)
    if aleatchuva == 0:
        chuva = 0
    weather.append(chuva)
    # print(chuva)
    if chuva >= 23:
        clientes_final = clientes_normal * 0.05
    elif chuva == 23:
        clientes_final = clientes_normal * 0.1
    elif chuva == 22:
        clientes_final = clientes_normal * 0.2
    elif chuva == 21:
        clientes_final = clientes_normal * 0.3
    elif chuva == 20:
        clientes_final = clientes_normal * 0.5
    elif chuva >= 16:
        clientes_final = clientes_normal * 0.6
    elif chuva >= 14:
        clientes_final = clientes_normal * 0.7
    elif chuva >= 13:
        clientes_final = clientes_normal * 0.8
    elif chuva >= 8:
        clientes_final = clientes_normal * 0.9
    elif chuva <= 7:
        clientes_final = clientes_normal

    if feriado == 1:
        clientes_final = clientes_final * 2
    
    loop += 1

    clientes.append(clientes_final)
    

# print(weather)
# print(clientes)

# clientes_total = [sum(clientes)]
# print(clientes_total)

clientes = list(map(int, clientes))
# print(clientes)