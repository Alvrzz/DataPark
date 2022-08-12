import requests
import datetime

# link para abrir open_weather: https://openweathermap.org/

now = datetime.datetime.now()
hour = now.hour
API_KEY = "241e22adb42697eaee0b5e8e6945d09a"
cidade = "Blumenau"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

if hour < 12:
    greeting = "Bom dia!"
elif hour < 18:
    greeting = "Boa tarde!"
else:
    greeting = "Boa noite!"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15
print(f"{format(greeting)} A previsão do tempo hoje em {cidade} é {descricao}, com a temperatura de {temperatura}ºC")