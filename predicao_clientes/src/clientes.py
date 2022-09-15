import holidays
from datetime import datetime
from src.database_connect import chuva_pred, data_pred

loop = 0
clientes_pred = []

while loop < len(chuva_pred):
    chuva_a = chuva_pred[loop]
    feriado_list = []
    dia_semana = datetime.today().isoweekday()
    clientes_normal = 600
    feriado = 0
    clientes_final = 0
    feriado_check = holidays.Brazil()
    if dia_semana == 6 or dia_semana == 7:
        feriado = 1
    for i in feriado_check['2022-01-01' : '2022-12-31']:
        feriado_list.append(i.isoformat())
    if data_pred in feriado_list:
        feriado = 1
    if feriado == 1:
        consta_feriado = 'Sim'
    if feriado == 0:
        consta_feriado = 'Não'
    if chuva_a >= 23:
        clientes_final = clientes_normal * 0.05
    elif chuva_a == 23:
        clientes_final = clientes_normal * 0.1
    elif chuva_a == 22:
        clientes_final = clientes_normal * 0.2
    elif chuva_a == 21:
        clientes_final = clientes_normal * 0.3
    elif chuva_a == 20:
        clientes_final = clientes_normal * 0.5
    elif chuva_a >= 16:
        clientes_final = clientes_normal * 0.6
    elif chuva_a >= 14:
        clientes_final = clientes_normal * 0.7
    elif chuva_a >= 13:
        clientes_final = clientes_normal * 0.8
    elif chuva_a >= 8:
        clientes_final = clientes_normal * 0.9
    elif chuva_a <= 7:
        clientes_final = clientes_normal

    if feriado == 1:
        clientes_final = clientes_final * 2
    
    loop += 1
    
    clientes_pred.append(clientes_final)

# print(clientes)