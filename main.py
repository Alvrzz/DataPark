# from previsao.main import previsao
# from limpeza.arquivos.limpeza_dados import limpeza1
# from limpeza.arquivos.limpeza_previsao import limpeza2
# # from database.main import GeraDatabase
# from predicao_clientes.main import PredicaoClientes
 


# GeraDatabase()
# print('Database enviado com sucesso.')
from limpeza.arquivos.limpeza_dados import limpeza1
limpeza1()
print('Limpeza e exportação  da base de dados concluida\n')
from previsao.main import previsao
previsao()
print('Previsão enviada com sucesso')
from limpeza.arquivos.limpeza_previsao import limpeza2
limpeza2()
print('Limpeza e exportação da base de previsão concluída.\n')
from predicao_clientes.main import PredicaoClientes
PredicaoClientes()
print('Predição de clientes e funcionários concluída com sucesso.')