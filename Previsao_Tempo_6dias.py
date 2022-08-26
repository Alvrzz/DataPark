from turtle import color
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs
import requests

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
# US english
LANGUAGE = "en-US,en;q=0.5"

def get_weather_data(url):
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html = session.get(url)
    # create a new soup
    soup = bs(html.text, "html.parser")
    # store all results on this dictionary
    result = {}
    # extract region
    result['region'] = soup.find("div", attrs={"id": "wob_loc"}).text
    # extract temperature now
    result['temp_now'] = soup.find("span", attrs={"id": "wob_tm"}).text
    # get the day and hour now
    result['dayhour'] = soup.find("div", attrs={"id": "wob_dts"}).text
    # get the actual weather
    result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text
    # get the precipitation
    result['precipitation'] = soup.find("span", attrs={"id": "wob_pp"}).text
    # get the % of humidity
    result['humidity'] = soup.find("span", attrs={"id": "wob_hm"}).text
    # extract the wind
    result['wind'] = soup.find("span", attrs={"id": "wob_ws"}).text
    # get next few days' weather
    next_days = []
    days = soup.find("div", attrs={"id": "wob_dp"})
    for day in days.findAll("div", attrs={"class": "wob_df"}):
        # extract the name of the day
        day_name = day.findAll("div")[0].attrs['aria-label']
        # get weather status for that day
        weather = day.find("img").attrs["alt"]
        temp = day.findAll("span", {"class": "wob_t"})
        # maximum temparature in Celsius, use temp[1].text if you want fahrenheit
        max_temp = temp[0].text
        # minimum temparature in Celsius, use temp[3].text if you want fahrenheit
        min_temp = temp[2].text
        next_days.append({"name": day_name, "weather": weather, "max_temp": max_temp, "min_temp": min_temp})
    # append to result
    result['next_days'] = next_days
    return result
    

if __name__ == "__main__":
    URL = "https://www.google.com/search?q=weather+blumenau&lr=lang_en&tbs=lr%3Alang_1en&sxsrf=ALiCzsaNKbuNAdCkdBIf_hZHbYCeppweEQ%3A1660566440526&ei=qDv6YsreH-LQ1sQP1b-zwAk&oq=wetaher+bluem&gs_lcp=Cgdnd3Mtd2l6EAEYADIJCAAQDRBGEIACMgYIABAeEA0yBggAEB4QDTIICAAQHhANEAoyBggAEB4QDTIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIICAAQHhAWEAoyBggAEB4QFjoMCCMQJxCdAhBGEIACOgQIIxAnOgQIABBDOggIABCABBCxAzoLCC4QgAQQxwEQ0QM6CwgAEIAEELEDEIMBOg4ILhCABBCxAxDHARDRAzoLCC4QgAQQsQMQgwE6CggAELEDEIMBEEM6BwgAELEDEEM6CgguEMcBENEDEEM6CQgAEMkDEAoQQzoFCAAQkgM6DgguEIAEEMcBENEDENQCOgoIABCABBDJAxAKOg0ILhCxAxDHARDRAxAKOgUILhCABDoHCC4QgAQQCjoFCAAQgAQ6BAguEEM6EggjELECEMkDECcQnQIQRhCAAjoKCAAQsQMQgwEQCjoECAAQCjoICAAQsQMQgwE6BwgAELEDEAo6EggAELEDEIMBEMkDEEMQRhCAAjoQCC4QsQMQxwEQ0QMQyQMQCjoECAAQDUoECEEYAEoECEYYAFAAWKQQYNEjaABwAXgAgAGhAogBqw2SAQYwLjEyLjGYAQCgAQHAAQE&sclient=gws-wiz"
    import argparse
    parser = argparse.ArgumentParser(description="Quick Script for Extracting Weather data using Google Weather")
    parser.add_argument("region", nargs="?", help="""Region to get weather for, must be available region.
                                        Default is your current location determined by your IP Address""", default="")
    # parse arguments
    args = parser.parse_args()
    region = args.region
    if region:
        region = region.replace(" ", "+")
        URL += f"+{region}"
    # get data
    data = get_weather_data(URL)
    # print data
    """print("Tempo em:", data["region"])
    print("Hoje:", data["dayhour"])
    print(f"Temperatura agora: {data['temp_now']}°C")
    print("Descrição:", data['weather_now'])
    print("Precipitacão:", data["precipitation"])
    print("Umidade:", data["humidity"])
    print("Vento:", data["wind"]) 
    print("Proximos dias:") """
    for dayweather in data["next_days"]:
        """ print("="*40, dayweather["name"], "="*40)
        print("Descrição:", dayweather["weather"])
        print(f"Temperatura Maxima: {dayweather['max_temp']}°C")
        print(f"Temperatura Minima: {dayweather['min_temp']}°C") """
        plt.scatter(x = dayweather['name'], y = float(dayweather['max_temp']), color='Red')
        plt.scatter(x = dayweather['name'], y = float(dayweather['min_temp']), color='Blue')


plt.suptitle("Previsão de Tempo em Blumenau")
plt.title("Clima nos próximos 6 dias")
plt.xlabel('Dias da Semana', fontsize=8) 
plt.ylabel('Temperatura Máxima e Mínima', fontsize=13)
plt.style.use('classic')
plt.show()