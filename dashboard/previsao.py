import sqlite3
import datetime
import timedelta 
from lxml import html
from bs4 import BeautifulSoup as bs
import requests

conn = sqlite3.connect('dashboard/previsao.db')
c = conn.cursor()

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
# US english
LANGUAGE = "en-US,en;q=0.5"

def obtem_dados_tempo(url):
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html = session.get(url)
    # Criar uma nova sopa
    sopa = bs(html.text, "html.parser")
    # Salvar os dados em esta biblioteca 
    resultado = {}
    # Extrai a região
    resultado['region'] = sopa.find("div", attrs={"id": "wob_loc"}).text
    # Extrai a temperatura agora
    resultado['temp_now'] = sopa.find("span", attrs={"id": "wob_tm"}).text
    # Obtem o dia e a hora agora
    resultado['dayhour'] = sopa.find("div", attrs={"id": "wob_dts"}).text
    # Obtem a previsao agora
    resultado['weather_now'] = sopa.find("span", attrs={"id": "wob_dc"}).text
    # Obtem a precipitacão
    resultado['precipitation'] = sopa.find("span", attrs={"id": "wob_pp"}).text
    # Obtem a % de umidade
    resultado['humidity'] = sopa.find("span", attrs={"id": "wob_hm"}).text
    # Obtem o vento 
    resultado['wind'] = sopa.find("span", attrs={"id": "wob_ws"}).text
    # Obtem a previsao dos proximos dias
    proximos_dias = []
    days = sopa.find("div", attrs={"id": "wob_dp"})
    for day in days.findAll("div", attrs={"class": "wob_df"}):
        # Obtem o nome do dia
        nome_do_dia = day.findAll("div")[0].attrs['aria-label']
        # Obtem o status para o dia
        tempo = day.find("img").attrs["alt"]
        temperatura = day.findAll("span", {"class": "wob_t"})
        # Tempetarua maxima em Celsius, use temp[1].si voce quiser em fahrenheit
        max_temp = temperatura[0].text
        # Temparature minima em Celsius, use temp[3].si voce quiser em fahrenheit
        min_temp = temperatura[2].text
        proximos_dias.append({"name": nome_do_dia, "weather": tempo, "max_temp": max_temp, "min_temp": min_temp})
    # Acrescenta no resultado
    resultado['next_days'] = proximos_dias
    return resultado
    

if __name__ == "__main__":
    URL = "https://www.google.com/search?q=weather+blumenau&lr=lang_en&tbs=lr%3Alang_1en&sxsrf=ALiCzsaNKbuNAdCkdBIf_hZHbYCeppweEQ%3A1660566440526&ei=qDv6YsreH-LQ1sQP1b-zwAk&oq=wetaher+bluem&gs_lcp=Cgdnd3Mtd2l6EAEYADIJCAAQDRBGEIACMgYIABAeEA0yBggAEB4QDTIICAAQHhANEAoyBggAEB4QDTIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIICAAQHhAWEAoyBggAEB4QFjoMCCMQJxCdAhBGEIACOgQIIxAnOgQIABBDOggIABCABBCxAzoLCC4QgAQQxwEQ0QM6CwgAEIAEELEDEIMBOg4ILhCABBCxAxDHARDRAzoLCC4QgAQQsQMQgwE6CggAELEDEIMBEEM6BwgAELEDEEM6CgguEMcBENEDEEM6CQgAEMkDEAoQQzoFCAAQkgM6DgguEIAEEMcBENEDENQCOgoIABCABBDJAxAKOg0ILhCxAxDHARDRAxAKOgUILhCABDoHCC4QgAQQCjoFCAAQgAQ6BAguEEM6EggjELECEMkDECcQnQIQRhCAAjoKCAAQsQMQgwEQCjoECAAQCjoICAAQsQMQgwE6BwgAELEDEAo6EggAELEDEIMBEMkDEEMQRhCAAjoQCC4QsQMQxwEQ0QMQyQMQCjoECAAQDUoECEEYAEoECEYYAFAAWKQQYNEjaABwAXgAgAGhAogBqw2SAQYwLjEyLjGYAQCgAQHAAQE&sclient=gws-wiz"
    import argparse
    parser = argparse.ArgumentParser(description="Quick Script for Extracting Weather data using Google Weather")
    parser.add_argument("region", nargs="?", help="""Region to get weather for, must be available region.
                                        Default is your current location determined by your IP Address""", default="")
    # Analisa os argumentos
    args = parser.parse_args()
    regiao = args.region
    if regiao:
        regiao = regiao.replace(" ", "+")
        URL += f"+{regiao}"
    # Obtem os dados
    dados = obtem_dados_tempo(URL)


def drop_table():
    c.execute("DROP TABLE IF EXISTS previsao")

        
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS previsao (Data, Dia_semana VARCHAR, Temp_Max TEXT, Temp_Min TEXT, mm_chuva_preci)") #<<<<<<<<<< CHANGED


drop_table()
create_table() #<<<<<<<<<< ADDED

conn.commit()

pagina = requests.get('https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/372/blumenau-sc')
arvore = html.fromstring(pagina.text)
milimetros = arvore.xpath('//span[@class="_margin-l-5"]/text()')  

y = -1
x = -1
dia_hj = datetime.date.today()
for tempododia in dados["next_days"]:  
    nome_dia = tempododia['name']
    max = tempododia['max_temp']
    min = tempododia['min_temp']
    x += 1
    y += 1
    mm_chuva = (milimetros[y])
    a = dia_hj + timedelta.Timedelta(days=x)     
    c.execute("INSERT INTO previsao (Data, Dia_semana, Temp_Max, Temp_min, mm_chuva_preci) VALUES (?, ?, ?, ?, ?)",
        (a, nome_dia, max, min, mm_chuva))
    conn.commit()


conn.close()