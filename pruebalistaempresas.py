import pandas_datareader as pdr
import matplotlib.pyplot as plt
import datetime 

empresas = ["AAPL", "AIG", "AMZN", "AXP", "BA", "BAC", "CAJ", "CAT", "CL", "CMCSA", "COP", "CSCO", "CVC", "CVS", "CVX", "DD", "DELL",
"F", "GD", "GE", "GS",  "GSK",  "HD", "HMC", "HPQ", "IBM", "JPM", "K", "KMB", "KO", "MAR", "MCD", "MMM", "MSFT", "NAV", 
"NOC", "NVS", "PEP", "PFE", "PG", "R", "RTN","SAP", "SNE", "SNY", "TM", "TOT", "TWX", "TXN", "TSLA" "UN", "VLO",  "WFC", "WMT", "XOM", "XRX","YHOO"]
print(empresas)

empresa = (input("Ingrese primera empresa que desea comparar: "))

if empresa in empresas:
    empresa2 = (input("Ingrese segunda empresa que desea comparar: "))

    if empresa2 in empresas and empresa != empresa2:

        end = datetime.datetime(2020,11,20).isoformat()
        start = datetime.datetime(2019,11,20).isoformat()
        print(start,end)

        y=empresa
        stock1 = pdr.get_data_yahoo(y, start=start, end=end)
        close1 = stock1['Close']
        print(stock1)
      

        x=empresa2
        stock2 = pdr.get_data_yahoo(x, start=start, end=end)
        close2 = stock2['Close']
        print(stock2)

        #Graficamos nuestra serie
        plt.plot(close1, color='b')
        plt.plot(close2, color='r')
        plt.show() #impresion dos graficos superpuestos 

    else:
        print("Ingrese una empresa de la lista y no repetir")


else:
    print("Ingrese una empresa del listado")   
    print(empresas) 

'''end = datetime.datetime(2020,11,20).isoformat()
start = datetime.datetime(2019,11,20).isoformat()
print(start,end)

y=empresa
stock1 = pdr.get_data_yahoo(y, start=start, end=end)
close1 = stock1['Close']
print(stock1)
plt.plot(close1, color='r')
plt.show()'''