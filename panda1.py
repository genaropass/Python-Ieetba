import pandas as pd
import io
import requests
import matplotlib.pyplot as plt
import numpy as np

url="https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Clase_4_datos/GOOGLE.csv"
s=requests.get(url).content
c=pd.read_csv(io.StringIO(s.decode('utf-8')))
data = c.to_dict("list")


x=data['Date']


# Se calcula la función sobre cada elemento por separado
y = data['Open']

plt.title("Opening values")

plt.xlabel('Años')


plt.plot(x, y, 'r')
plt.show()