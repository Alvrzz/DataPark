from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily

# Periodo para o resultado
data_inicio = datetime(2019, 1, 1)
data_termina = datetime(2019, 1, 15)

# Localizacao Cordenadas 
location = Point(-26.9187, -49.066 )

# Obten dados das datas selecionadas
data = Daily(location, data_inicio, data_termina)
data = data.fetch()

data.plot(y=['tmin', 'tmax'])
print (data)

