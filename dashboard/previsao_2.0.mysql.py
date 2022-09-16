import mysql.connector
import datetime
import timedelta
from lxml import html
from bs4 import BeautifulSoup as bs
import requests

# Connecta ao banco de dados.
conn = mysql.connector.connect(
    host = '3.89.36.150',
    user = 'e2122g4',
    password = 'e2122g4@16@ago',
    database = 'e2122g4'
    )
c = conn.cursor()

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
# Ingles Americano.
LANGUAGE = "en-US,en;q=0.5"

# Define especificamente cada dado no qual sera extraido.
def obtem_dados_tempo(url):
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html = session.get(url)
    # Criar uma nova sopa.
    sopa = bs(html.text, "html.parser")
    # Salvar os dados em esta biblioteca. 
    resultado = {}
    # Extrai a região.
    resultado['region'] = sopa.find("div", attrs={"id": "wob_loc"}).text
    # Extrai a temperatura agora.
    resultado['temp_now'] = sopa.find("span", attrs={"id": "wob_tm"}).text
    # Obtem o dia e a hora agora.
    resultado['dayhour'] = sopa.find("div", attrs={"id": "wob_dts"}).text
    # Obtem a previsao agora.
    resultado['weather_now'] = sopa.find("span", attrs={"id": "wob_dc"}).text
    # Obtem a previsao dos proximos dias.
    proximos_dias = []
    days = sopa.find("div", attrs={"id": "wob_dp"})
    for day in days.findAll("div", attrs={"class": "wob_df"}):
        # Obtem o nome do dia.
        nome_do_dia = day.findAll("div")[0].attrs['aria-label']
        # Obtem o status para o dia.
        tempo = day.find("img").attrs["alt"]
        temperatura = day.findAll("span", {"class": "wob_t"})
        # Tempetarua maxima em Celsius, use temp[1].si voce quiser em fahrenheit.
        max_temp = temperatura[0].text
        # Temparature minima em Celsius, use temp[3].si voce quiser em fahrenheit.
        min_temp = temperatura[2].text
        proximos_dias.append({"name": nome_do_dia, "weather": tempo, "max_temp": max_temp, "min_temp": min_temp})
    # Acrescenta no resultado.
    resultado['next_days'] = proximos_dias
    return resultado
    
    # Pagina de extracao do dia das semana, temperatura maxima e temperatura minima.
if __name__ == "__main__":
    URL = "https://www.google.com/search?q=weather+blumenau&lr=lang_en&tbs=lr%3Alang_1en&sxsrf=ALiCzsaNKbuNAdCkdBIf_hZHbYCeppweEQ%3A1660566440526&ei=qDv6YsreH-LQ1sQP1b-zwAk&oq=wetaher+bluem&gs_lcp=Cgdnd3Mtd2l6EAEYADIJCAAQDRBGEIACMgYIABAeEA0yBggAEB4QDTIICAAQHhANEAoyBggAEB4QDTIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIICAAQHhAWEAoyBggAEB4QFjoMCCMQJxCdAhBGEIACOgQIIxAnOgQIABBDOggIABCABBCxAzoLCC4QgAQQxwEQ0QM6CwgAEIAEELEDEIMBOg4ILhCABBCxAxDHARDRAzoLCC4QgAQQsQMQgwE6CggAELEDEIMBEEM6BwgAELEDEEM6CgguEMcBENEDEEM6CQgAEMkDEAoQQzoFCAAQkgM6DgguEIAEEMcBENEDENQCOgoIABCABBDJAxAKOg0ILhCxAxDHARDRAxAKOgUILhCABDoHCC4QgAQQCjoFCAAQgAQ6BAguEEM6EggjELECEMkDECcQnQIQRhCAAjoKCAAQsQMQgwEQCjoECAAQCjoICAAQsQMQgwE6BwgAELEDEAo6EggAELEDEIMBEMkDEEMQRhCAAjoQCC4QsQMQxwEQ0QMQyQMQCjoECAAQDUoECEEYAEoECEYYAFAAWKQQYNEjaABwAXgAgAGhAogBqw2SAQYwLjEyLjGYAQCgAQHAAQE&sclient=gws-wiz"
    import argparse
    parser = argparse.ArgumentParser(description="Quick Script for Extracting Weather data using Google Weather")
    parser.add_argument("region", nargs="?", help="""Region to get weather for, must be available region.
                                        Default is your current location determined by your IP Address""", default="")
    # Analisa os argumentos.
    args = parser.parse_args()
    regiao = args.region
    if regiao:
        regiao = regiao.replace(" ", "+")
        URL += f"+{regiao}"
    # Obtem os dados.
    dados = obtem_dados_tempo(URL)

# define oque sera deletado no banco de dados, neste caso a tabela previsao. 
def drop_table():
    c.execute("""DROP TABLE IF EXISTS PREVISAO""")

# define a criacao da  tabela.        
def create_table():
    c.execute("""
    CREATE TABLE PREVISAO(
        PREVISAO_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
        DATA DATE NOT NULL,
        DIA_SEMANA TEXT NOT NULL,
        TEMP_MAX TEXT NOT NULL, 
        TEMP_MIN TEXT NOT NULL,
        MM_CHUVA_PRECI TEXT NOT NULL
        );
""")


drop_table() # Deleta a tabela.
create_table() # Cria novamente a tabela.

conn.commit()

# Pagina para extracao do Milimetro de chuva.
pagina = requests.get('https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/372/blumenau-sc')
arvore = html.fromstring(pagina.text)
milimetros = arvore.xpath('//span[@class="_margin-l-5"]/text()')  

y = -1 # Junto com o y+=1 e mm_chuva = (milimetros[y]) adiciona o milimetros de chuva no restante dos dias da semana no banco de dados.
x = -1 # Junto com o x+=1 e  a = dia_hj + timedelta.Timedelta(days=x) adiciona o restante das datas dos dias da semana no banco de dados.
dia_hj = datetime.date.today()
for tempododia in dados["next_days"]:  
    nome_dia = tempododia['name']
    max = tempododia['max_temp']
    min = tempododia['min_temp']
    x += 1
    y += 1
    mm_chuva = (milimetros[y])
    a = dia_hj + timedelta.Timedelta(days=x)   
    # Insere todos os dados no banco de dados da previsao do tempo.  
    sql = ('INSERT INTO PREVISAO ( DATA, DIA_SEMANA,TEMP_MAX,TEMP_MIN, MM_CHUVA_PRECi) VALUES (%s, %s, %s, %s, %s)')
    val = a, nome_dia, max, min, str(mm_chuva)
    c.execute(sql, val)
    conn.commit()
    
   

conn.close()