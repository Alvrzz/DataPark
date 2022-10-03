'''
Este aplicativo roda o código de gerar previsão do clima e de clientes todo dia as 6 da manhã.
'''

from apscheduler.schedulers.background import BlockingScheduler

def rodarCoisas():
    from previsao.main import previsao
    previsao()
    print('Previsão enviada com sucesso\n')
    from limpeza.arquivos.limpeza_previsao import limpeza2
    limpeza2()
    print('Limpeza e exportação da base de previsão concluída.\n')
    from predicao_clientes.main import PredicaoClientes
    PredicaoClientes()
    print('Predição de clientes e funcionários concluída com sucesso.')

sched = BlockingScheduler()

sched.add_job(rodarCoisas, 'cron', hour= 6)

sched.start()