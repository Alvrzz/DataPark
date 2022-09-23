# Roteiro
### Estudo do caso
Em um determinado parque da nossa região os gestores estavam enfrentando problemas com a alocação de mão de obra, principalmente em razão da alternância de público nos dias de chuva. Para tal, buscamos levantar dados históricos levando em consideração a pluviometria e o número de visitantes por dia.
Após evidenciar o problema, buscamos uma solução utilizando a previsão de chuva futura e sugerindo ainda um quadro de funcionários ideal para os próximos dias.   

### Banco de dados
Para dados históricos consideramos a construção de um banco de dados ficticio. O banco de dados é formado pelas tabelas:

#### Tabela Atracoes:
- Cadastro simples de 18 atrações do parque para alocação de funcionários, bem como localização das mesmas.

#### Tabela Cidades: 
- Cadastro de todas as cidades brasileiras, bem como UF à que pertencem.

#### Tabela Clima: 
- Cadastro de dados históricos fictícios dos anos de 2019,2020,2021, dia a dia, registrando quanto choveu em mm (milímetros).
- Foram feitas as seguintes considerações:
- Chuva num range randômico de 0 a 30, sendo 0 nenhuma chuva e 30 um dia bastante chuvoso.

#### Tabela Funcionarios:
- Cadastro de todos os funcionários que trabalharam em cada dia, no mesmo período da pesquisa, bem como alocação por setor.
- Considerado 5 pessoas por setor do parque, sendo 18 setores, no período de 1096 dias.

#### Tabela clientes:
- Cadastro de todos os clientes que visitaram o parque no mesmo período da pesquisa, considerando:
- Atribuido de forma randômica cidade e estado de origem de cada visitante.
- Consideramos uma visitação inicial de 600 pessoas por dia, corrigindo este número de acordo com a pluviometria estabelecidade para este dia.
- Todo sábado, domingo e feriado, essa visitação dobrou.
- A partir daqui, toda a base foi tratada para recalcular a visitação de cada dia, considerando o fator chuva (mm). Nos dias com pluviometria próxima de zero, afetando menos, e conforme esse índice aumentou e se aproximou de 30, chegando a zerar a visitação do parque nesse dia.
- Essa tabela conta ainda com o campo  Cliente_idade, para disponibilizar dados sobre a faixa etária dos visitantes, e também o campo Cliente_CPF, gerado aleatoriamente.

### WebScraping
#### Tabela previsão:
- Previsão do tempo de 8 dias, incluindo data, dia da semana, temperatura máxima, temperatura mínima, milímetros de chuva e precipitação. 

### Tratamento e Análise

### Dashboard

