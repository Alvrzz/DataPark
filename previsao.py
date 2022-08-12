import requests
import datetime

# link para abrir open_weather: https://openweathermap.org/

API_KEY = "241e22adb42697eaee0b5e8e6945d09a"
agora = datetime.datetime.now()
hora = agora.hour
cidade = "Blumenau"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

if hora < 12:
    saudacao = "Bom dia!"
elif hora < 18:
    saudacao = "Boa tarde!"
else:
    saudacao = "Boa noite!"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15
print(f"{format(saudacao)} A previsão do tempo hoje em {cidade} é {descricao}, com a temperatura de {round(temperatura)}ºC")