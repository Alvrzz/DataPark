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

Certa empresa apresenta dificuldades para alocação de equipe em determinados eventos, resultando em alocações excessivas de funcionários para o evento, gerando um grande prejuízo que poderia ter sido evitado. Após diversas reclamações de visitantes alegando que o atendimento estava escasso, notou-se que estava faltando funcionários para suprir a demanda.

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
cliente_uf string
cliente_cidade string

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

