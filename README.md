# 📊Projeto Grupo 4 - Analise de Dados - Entra21📊
**Time**: 

**Luan Alvarez** (Scrum Master , Limpeza, Analise e DashBoards) 
- [linkedin](https://www.linkedin.com/in/luan-alvarez-1499a7224/); 
- [Whatsapp](https://wa.me/+55013991378334)

**William Justino** (Ação)
- [linkedin](https://www.linkedin.com/in/william-justino-analista-de-dados/);
- [Whatsapp](https://wa.me/+55048998066865)

**Jean Carlos Bernabé De Oliveira** (Banco de dados)
- [linkedin](https://www.linkedin.com/search/results/all/?heroEntityKey=urn%3Ali%3Afsd_profile%3AACoAAAo8S9UB11_f9sQcqx5RD90PLCQdV23EGgA&keywords=jean%20carlos%20bernab%C3%A9%20de%20oliveira&origin=RICH_QUERY_TYPEAHEAD_HISTORY&position=0&searchId=cfaf2dad-fc0e-4d27-8fb7-51a49c7d52e7&sid=iHb);
- [Whatsapp](https://wa.me/+43991898626)


**Gabriel Mello** (Banco de dados)
-  [linkedin](https://www.linkedin.com/in/gabriel-mello-analise-de-dados-python-sql/)
-  [Whatsapp](https://wa.me/+55048996736618)

**Gustavo Rodrigues Da Silva** (Limpeza, Analise e DashBoards)
- [linkedin](https://www.linkedin.com/in/guhtcha/);
- [Whatsapp](https://wa.me/+55053984742009).

**Lucas Locks** (Ação) 
-  [linkedin](https://www.linkedin.com/in/lucas-locks-analista-de-dados/), 
-  [Whatsapp](https://wa.me/+55049999367658)

### **Sobre:**

Estudo de Tendência e previsão de público para alocação de equipes.
Assertividade na contratação de mão de obra usando como base dados históricos e previsão futura.

Através de análise de dados históricos de visitação do parque, cruzando essas informações com os dados climáticos. Banco simulado em python e mysql para construção de indicadores, considerando variáveis como datas de maiores visitas, épocas do ano, e quantidade de atrações. Observar como a visitação no parque diminui consideravelmente em dias de chuva.
Ferramenta que exibirá de maneira gráfica essa informação, e em seguida, usará como base previsão de tempo futura para sugerir uma adequação na locação de mão de obra.

### **O problema:**

A empresa apresenta dificuldades para alocação de equipe em determinados eventos, resultando em alocações excessivas gerando um prejuízo que pode ser evitado.

### **FLUXOGRAMA**
![Fluxograma3](https://user-images.githubusercontent.com/104404936/188039563-a2a3f779-b98d-4e51-80e5-3b750dae27ba.jpg)


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


## Limpeza e Analise
### Limpeza do Banco de Dados

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



### Limpeza da base de previsão

Arquivo executável de limpeza do WebScraping e atualização da tabela na nuvem.

* Importação:  Conexão com a base de dados da aplicação WebScraping para tratamento com mysql.connector

* Limpeza:  Remoção de colunas e tabelas não complementares para analise(ID, TEMP_MAX, TEMP_MIN, DIA_SEMANA);
            Divisão de coluna(MM_CHUVA_PRECI) em duas colunas(PREVISAO_CHUVA & PREVISAO_PREVISAO) de dados int;
            Alteração dos tipos de dados (PREVISAO_CHUVA & PREVISAO_PREVISAO);
            Alteração dos nomes das colunas(DATA para PREVISAO_DATA) para melhor vizualização;
            Remoção de caracteres ('mm' & '%') das colunas DATA E PREVISAO_DATA.
* Exportação: 
            Envio da nova tabela(PREVISAO_TRATADA) para o banco de dados MySQL.








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









