from faker import Faker
from chuva_clientes.chuva import clientes

nomes = []
faker = Faker('pt_BR')

for i in range(sum(clientes)):
    nomes.append(f'{faker.first_name()} {faker.last_name()}')

# print(nomes)
