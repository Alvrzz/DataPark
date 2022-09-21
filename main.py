from dashboard.main import previsao
from limpeza.arquivos.limpeza_dados import limpeza1
from limpeza.arquivos.limpeza_previsao import limpeza2
# from database.main import GeraDatabase
from predicao_clientes.main import PredicaoClientes



# GeraDatabase()
# print('Database enviado com sucesso.')

#limpeza1()
#print('Limpeza e exportação  da base de dados concluida\n')

# previsao()
# print('Previsão enviada com sucesso')

# limpeza2()
# print('Limpeza e exportação da base de previsão concluída.\n')

PredicaoClientes()
print('Predição de clientes e funcionários concluída com sucesso.')