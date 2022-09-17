### Web Scraping Previsão Tempo ###

Arquivo executável com a finalidade de importar através do metodo web scraping a previsão do tempo de 8 dias e exportar os dados para a nuvem.

* Importação:  Através das bibliotecas “ from lxml import html “ e “ from bs4 import BeautifulSoup as bs” para a importação de  códigos em html para o python e o modulo “ import requests “  para leitura e compressão humana em python. Através da biblioteca “ datetime “ a utilização para a importação dos dias pela sequência “ dia/mês/ano” .
 
*Limpeza:  Utilização do python para limpeza e simplificação da tabela.
Utilização da biblioteca “ import timedelta “ para adicionar 7 dias adicionais no tratamento da previsão além do dia atual.


* Exportação:  Utilização do mysql.connector para exportar os dados limpos.
              Comandos em SQL para criação de uma nova tabela na nuvem (PREVISAO).  
