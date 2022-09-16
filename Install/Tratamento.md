### Tratamento do Banco de Dados

Arquivo executavel com a finalidade de importar da nuvem, limpar e exportar os dados para a nuvem.

* Importação: Conexão com a base de dados na nuvem via mysql.connector, conectando com as tabelas existentes na nuvem;
              Utilização de comandos SQL para armazenamento das tabelas em váriaveis distintas.              

* Limpeza:  Utilização do pandas para limpeza e simplificação da tabela;
            Utilização da função Groupby para contabilizar a quantidade de clientes(CLIENTE_DATA) e funcionarios(FUNCIONARIOS_DATA) por data;
            Utilização da função merge e join para conexão das tabelas(CLIMA, FUNCIONARIOS, CLIENTES);
            Seleção de colunas e tabelas complementares para analise(CLIMA, FUNCIONARIOS, CLIENTES), removendo colunas não necessarias;
            Alteração dos nomes das colunas para melhor vizualização(CLIENTES_DATA para TABELA_CLIENTES, FUNCIONARIOS_DATA para TABELA_FUNCIONARIOS, CLIMA_CHUVA_MM para TABELA_CHUVA):

* Exportação: Utilização do mysql.connector para exportar os dados limpos.
              Comandos em SQL para criação de uma nova tabela na nuvem (TABELA_GERAL).  



### Tratamento previsão

Arquivo executável de tratamento do WebScraping e atualização da tabela na nuvem.

* Importação:  Conexão com a base de dados da aplicação WebScraping para tratamento com mysql.connector

* Limpeza:  Remoção de colunas e tabelas não complementares para analise(ID, TEMP_MAX, TEMP_MIN, DIA_SEMANA);
            Divisão de coluna(MM_CHUVA_PRECI) em duas colunas(PREVISAO_CHUVA & PREVISAO_PREVISAO) de dados int;
            Alteração dos tipos de dados (PREVISAO_CHUVA & PREVISAO_PREVISAO);
            Alteração dos nomes das colunas(DATA para PREVISAO_DATA) para melhor vizualização;
            Remoção de caracteres ('mm' & '%') das colunas DATA E PREVISAO_DATA.
* Exportação: 
            Envio da nova tabela(PREVISAO_TRATADA) para o banco de dados MySQL.