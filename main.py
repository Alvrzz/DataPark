from dashboard.main import obtem_dados_tempo, drop_table, create_table, web_scraping
from limpeza.arquivos.limpeza_dados import limpeza1
from limpeza.arquivos.limpeza_previsao import limpeza2



#CriaTabelas()
#EnviaDatabase()
#print('Database enviado com sucesso.')

limpeza1()
print('Limpeza e exportação  da base de dados concluida\n')

obtem_dados_tempo()
print('Dados da previsão do tempo obtidos com sucesso!\n')

drop_table()
create_table()
print('Tabela criada com sucesso.\n')

web_scraping()
print('Dados da previsão inseridos com sucesso nas tabelas.\n')

limpeza2()
print('Limpeza e exportação da base de previsão concluída.\n')
