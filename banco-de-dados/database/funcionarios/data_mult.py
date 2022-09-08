from funcionarios.data import data

data_mult_funcionarios = []
loop = 0

while loop < 1096:
    data_mult_funcionarios.extend([data[loop]] * 90)
    loop += 1