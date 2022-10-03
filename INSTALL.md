# Instalação do database, análise dos dados e previsão de clientes e funcionários.

1. Crie ou utilize um servidor MySQL para armazenar os dados;
2. Crie um arquivo chamado "local_settings.py" dentro da pasta "configurações", que está na pasta raiz da aplicação;
3. Dentro deste arquivo coloque as variáveis "hostip, usuario, senha, databasename";
    * hostip: O ip do host do database;
    * usuario: O usuário de acesso ao database;
    * senha: A senha do usuário acima;
    * databasename: Nome da database para fazer a conexão;
    * **(Todas as variáveis devem ser formatadas como *string*)**
4. Concluindo estes passos é apenas rodar o arquivo "main.py" que se encontra na pasta raiz da aplicação;
    * Caso for de seu desejo, após rodar o "main.py" você pode rodar o "main_auto.py" que todo o dia as 6 da manhã ele fará a previsão de funcionários e clientes para o parque.