from CHUVA import clientes
from DATA import data

data_mult = []
loop = 0

while loop < 1096:
    data_mult.extend([data[loop]] * clientes[loop])
    loop += 1

# print(len(data_mult))