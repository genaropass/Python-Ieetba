#Armar un programa donde se analize la información de ciertas empresas (entrada del usuario) y se las grafique comparativamente.

#El usuario debe poder seleccionar empresas de una lista de opciones y el programa debe calcular las intersecciones entre los
#precios de ambas. Se debe permitir graficar esta información de forma gráfica y almacenar en un archivo de excel las fechas donde
#ocurrieron las intersecciones.
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import datetime 
import pandas as pd

pregunta=(input("desea ingresar al sistema?"))

while pregunta == "si" or pregunta == "SI" or pregunta == "Si":

    print("BIENVENIDO PROGRAMA DE COMPARACION DE ACCIONES MERCADO FINANCIERO")
    print("\n")
    print("Seleccione empresas de la lista en mayuscula" )

    empresas = ["AAPL", "AIG", "AMZN", "AXP","CMCSA", "COP", "CSCO","DELL", "F", "GD", "GE", "GS",  "GSK",  "HD",
    "HMC", "HPQ", "IBM","MSFT", "NAV","NOC","TSLA","YHOO", "GOOG"]
    print(empresas)

    empresa = str(input("Ingrese empresa a comparar: "))

    if empresa in empresas:
        
        empresa2= str(input("Ingrese segunda empresa a comparar: "))

        if empresa2 in empresas and empresa != empresa2:
            #dentro de este if creamos la comparacion y los graficos de las dos empresas mostrando 
            #google de color azul y amazon de color rojo 

            #fUNCION FECHA QUE USUARIO DESEA
            def comprobar_fechain(fechain):
                try:
                    datetime.datetime.strptime(fecha, "%d-%m-%Y")
                except:
                    return "El formato debe ser  DD-MM-YYYY"
                return datetime.datetime.strptime(fecha, '%d-%m-%Y')

            fechain = input("Dame fecha hasta donde quiere comparar precios")

            print (comprobar_fechain(fechain))

            def comprobar_fechaout(fechaout):
                try:
                    datetime.datetime.strptime(fecha, "%d-%m-%Y")
                except:
                    return "El formato debe ser  DD-MM-YYYY"
                return datetime.datetime.strptime(fecha, '%d-%m-%Y')

            fechaout = input("Dame una fecha de inicio de donde quiere comparar precios")    

            print (comprobar_fechaout(fechaout))
                            
            #DEFINIMOS FECHA DE NUESTROS GRAFICOS 
            end = datetime.datetime.strptime(fechain, "%d-%m-%Y").isoformat()
            start = datetime.datetime.strptime(fechaout, "%d-%m-%Y").isoformat()
            print(start,end)

            #ACCIONES
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
            plt.grid()
            plt.xlabel('Eje de las x')
            plt.ylabel('Eje de las y')
            plt.show() #impresion dos graficos superpuestos 
        else:
            print("Ingrese una empresa de la lista y no repetir")  

    else:
        print("Debe ingresar el nombre de empresas de la lista para que el programa funcione")


    last=input("Desea hacer otra consulta?")

    if last == "no" or last == "NO" or last == "No" or last == "nO":
        break
        print("Muchas gracias")
else: 
    print("Muchas gracias")
