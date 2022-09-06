import pandas as pd
from CHUVA import clientes
from random import randint

tabela_cidade = ('https://docs.google.com/spreadsheets/d/e/2PACX-1vSGBot2EFAMNJRdwUVK3ou7lC0uQcZE3X9NqUaVJmgd778ZVSJAAVljtZPG3eHEseo2pZQ4HKITGWZ1/pub?gid=536340842&single=true&output=csv')
colunas = list(['ID', 'UF', 'Municipio'])
df = pd.read_csv(tabela_cidade, index_col=0, header=0, usecols=colunas)
numcidades = list((df.shape))[0]\

cidade_id = []
loop = 0

while loop < sum(clientes):
    cidade_id.append(randint(1, numcidades))
    loop += 1

# print(len(cidade_id))