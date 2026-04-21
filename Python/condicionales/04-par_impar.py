"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""

num = int(input("Ingrese un numero entero: "))

if num % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

"""
Ya me sabia el operador del modulo que da el residuo de la operacion, si es siempre 0 pues va a ser par
porque si es impar siempre el residuo sera de 1 porque no dan enteros, asi que esta facil :)
"""