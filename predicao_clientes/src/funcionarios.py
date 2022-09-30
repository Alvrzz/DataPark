from predicao_clientes.src.database_connect import chuva_pred
from predicao_clientes.src.clientes import clientes_pred

funcionarios_normal = 90
loop = 0
funcionarios_pred = []

while loop < len(chuva_pred):
    chuva_a = chuva_pred[loop]
    if chuva_a >= 24:
        funcionarios_final = funcionarios_normal * 0.40
    elif chuva_a == 23:
        funcionarios_final = funcionarios_normal * 0.45
    elif chuva_a == 22:
        funcionarios_final = funcionarios_normal * 0.50
    elif chuva_a == 21:
        funcionarios_final = funcionarios_normal * 0.55
    elif chuva_a == 20:
        funcionarios_final = funcionarios_normal * 0.60
    elif chuva_a >= 16:
        funcionarios_final = funcionarios_normal * 0.65
    elif chuva_a >= 14:
        funcionarios_final = funcionarios_normal * 0.7
    elif chuva_a >= 13:
        funcionarios_final = funcionarios_normal * 0.8
    elif chuva_a >= 8:
        funcionarios_final = funcionarios_normal * 0.9
    elif chuva_a <= 7:
        funcionarios_final = funcionarios_normal
    if clientes_pred[loop] > 600:
        funcionarios_final = 90
    if clientes_pred[loop] == 1200:
        funcionarios_final = 120
    loop += 1

    funcionarios_pred.append(int(funcionarios_final))