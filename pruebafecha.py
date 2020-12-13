import datetime

'''while True:
    try:
        fecha = input("Introducir Fecha dd-mm-aaaa: ")
        fecha = datetime.datetime.strptime(fecha, "%d-%m-%Y")
        break
 
    except:
        print ("Fecha incorrecta\n")

print(fecha)'''

def comprobar_fecha(fecha):
    try:
        datetime.datetime.strptime(fecha, "%d-%m-%Y")
    except:
        return "El formato debe ser  DD/MM/YYYY"
    return datetime.datetime.strptime(fecha, '%d-%m-%Y')

fecha = input("Dame una fecha")

print (comprobar_fecha(fecha))