from dashboard.main import obtem_dados_tempo, drop_table, create_table, web_scraping
from tratamento_dados.main import tratamento1,tratamento2

# CriaTabelas()
# EnviaDatabase()
# print('Database enviado com sucesso.')

tratamento1()
print('Limpeza e exportação  da base de dados concluida\n')

obtem_dados_tempo()
print('Dados da previsão do tempo obtidos com sucesso!\n')

drop_table()
create_table()
print('Tabela criada com sucesso.\n')

web_scraping()
print('Dados da previsão inseridos com sucesso nas tabelas.\n')

tratamento2()
print('Limpeza e exportação da base de previsão concluída.\n')
