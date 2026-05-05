"""
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	            Tipo impositivo
Menos de 10000€	        5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	        45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le 
corresponde.
"""
renta = int(input("Ingrese su renta anual: "))

if renta < 10000:
    print("Su impositivo es: 5%")
elif renta >= 10000 and renta <= 20000:
    print("Su impositivo es: 15%")
elif renta >= 20000 and renta <= 35000:
    print("Su impositivo es: 20%")
elif renta >= 35000 and renta <= 60000:
    print("Su impositivo es: 30%")
else:
    print("Su impositivo es: 45%")

"""
En este ejercicio aprendi a usar elif, es como un else y un if ya que en el else no puedes poner una condicion
pero con elif, es como que sigue evaluando y puedes poner una nueva condicion. Tambien uso el operador and
para comparar entre dos condiciones :)
"""
