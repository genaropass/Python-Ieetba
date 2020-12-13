import pandas_datareader as pdr
import matplotlib.pyplot as plt
import datetime 
import pandas as pd
import pandas as pds
from collections import Counter


accion = input("agrege empresa")
accion2 = input("agregre otra empresa")

#print (accion + ".csv")

datos = pd.read_csv(accion + ".csv")
datos2 = pd.read_csv(accion2 + ".csv")

d = datos.to_dict("list")
a = datos2.to_dict('list')

d = d['Close']
a = a['Close']

print(d)

print("\n")

print(a)
#def comparar_listas(d,a):
 #   return Counter (d) == Counter(a)   {para comparar si hay elementos en dos listas con true o false}
#print(comparar_listas(d,a))

#print(d)

#print('\n')

#print (a)


   

#print(datos['Open'])


'''#DEFINIMOS FECHA DE NUESTROS GRAFICOS 
end = datetime.datetime(2020,11,20).isoformat()
start = datetime.datetime(2019,11,20).isoformat()
print(start,end)


y='AMZN'
stock1 = pdr.get_data_yahoo(y, start=start, end=end)
close1 = stock1['Close']
print(stock1)
#Graficamos nuestra serie
#plt.plot(close, color='b')
#plt.show()
x='GOOG'
stock2 = pdr.get_data_yahoo(x, start=start, end=end)
close2 = stock2['Close']
print(stock2)
#Graficamos nuestra serie
plt.plot(close1, color='b')
plt.plot(close2, color='r')
plt.show() #impresion dos graficos superpuestos '''



