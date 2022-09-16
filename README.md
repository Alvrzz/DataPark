# 📊Projeto Grupo 4 - Analise de Dados - Entra21📊
**Time**: 

- **Luan Alvarez** (Scrum Master , Tratamento e Analise),

- **William Justino** (Ação),

- **Jean Carlos Bernabé De Oliveira** (Banco de dados),

- **Gabriel Mello** (Banco de dados), 

- **Gustavo Rodrigues Da Silva** (Tratamento e Analise), 

- **Lucas Locks** (Ação) 

### **Sobre:**

Estudo de Tendência e previsão de público para alocação de equipes.
Assertividade na contratação de mão de obra usando como base dados históricos e previsão futura.

Através de análise de dados históricos de visitação do parque, cruzando essas informações com os dados climáticos. Banco simulado em python e mysql para construção de indicadores, considerando variáveis como datas de maiores visitas, épocas do ano, e quantidade de atrações. Observar como a visitação no parque diminui consideravelmente em dias de chuva.
Ferramenta que exibirá de maneira gráfica essa informação, e em seguida, usará como base previsão de tempo futura para sugerir uma adequação na locação de mão de obra.

### **O problema:**

A empresa apresenta dificuldades para alocação de equipe em determinados eventos, resultando em alocações excessivas ou até mesmo escassez de funcionários para eventos específicos, gerando um prejuízo que pode ser evitado.

### **Backlog:**

- Banco de dados gerado com python
  - Registro dos dados do clima. 
  - Registro de acessos diários clientes
  - Registro de funcionários
  - Atrações

- Tratamento de dados
  - Limpeza e destacar dados relevantes para o problema 

- Analise

  - Analise com python

    - SeaBorn e MatplotLib

  - Conclusões

    

- Compartilhamento
  - Gerar dashboards
    - Compartilhamento da analise de maneira intuitiva

- Ação
  - Tomar decisões com base nos dados compartilhados de maneira intuitiva.


### **FLUXOGRAMA**


![Fluxograma3](https://user-images.githubusercontent.com/104404936/188039563-a2a3f779-b98d-4e51-80e5-3b750dae27ba.jpg)



### **DER:** 


Clima
-
clima_id PK int
clima_data string
clima_chuvamm int
clima_tempmin real
clima_tempmax real

Clientes
-
cliente_id pk int
cliente_data string
cliente_nome string
cliente_cpf string
cliente_idade int
cliente_uf string
cliente_cidade_id FK >- Cidades.cidade_id int

Cidades
-
cidade_id pk int
cidade_nome string
cidade_uf string


Funcionarios
-
funcionario_id pk int
funcionario_data string
funcionario_nome string
funcionario_area string
funcionario_atracoes_id FK >- Atracoes.atracao_id int

Atracoes
-
atracao_id pk int
atracao_nome string


### **Parâmetros banco simulado:**


- Tabela Atracoes:

  - Cadastro simples de 18 atrações do parque para alocação de funcionários, bem como localização das mesmas.


- Tabela Cidades: 

  - Cadastro de todas as cidades brasileiras, bem como UF à que pertencem.


- Tabela Cima: 

  - Cadastro de dados históricos fictícios dos anos de 2019,2020,2021, dia a dia, registrando quanto choveu em mm (milímetros), temperatura mínima e máxima de cada dia.
  - Foram feitas as seguintes considerações:
    - Chuva num range randômico de 0 a 30, sendo 0 nenhuma chuva e 30 um dia bastante chuvoso.
    - Para temperaturas máximas e mínimas, trabalhamos com duas faixas de range, uma para meses mais quentes (nov_abr), e outra para os frios (mai_out).


- Tabela Funcionarios:

  -  Cadastro de todos os funcionários que trabalharam em cada dia, no mesmo período da pesquisa, bem como alocação por setor.
  -  Considerado 5 pessoas por setor do parque, sendo 18 setores, no período de 1096 dias.

- Tabela clientes:

  - Cadastro de todos os clientes que visitaram o parque no mesmo período da pesquisa, considerando:
    -  50% dos visitantes originalmente do estado de Santa Catarina, e os demais, distribuídos de forma randômica entre todos os estados.
    -  Nos meses de calor (nov_abr) consideramos uma visitação original de 600 pessoas por dia, e 400 pessoas por dia para os meses mais frios. 
    -  Todo sábado domingo, e feriado, essa visitação dobrou.
    -  A partir daqui, toda a base foi tratada para recalcular a visitação de cada dia, considerando o fator chuva (mm). Nos dias com pluviometria próxima de zero, afetando menos, e conforme esse índice aumentou e se aproximou de 30, chegando a zerar a visitação do parque nesse dia.
  - Essa tabela conta ainda com o campo Cidade_id, para que se possa fazer busca de origem do visitante, o campo Cliente_idade, para disponibilizar dados sobre a faixa etária dos visitantes, e também o campo Cliente_CPF, gerado aleatoriamente.


## Tratamento e Analise
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












