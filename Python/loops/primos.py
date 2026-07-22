"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
"""

numero = int(input("Ingrese un numero entero: "))

divisores = 0

for i in range(1, numero + 1):
    if (numero % i == 0):
        print(f"Numero divisible entre {i}")
        divisores += 1

if divisores == 2:
    print("Numero es primo")
else:
    print("Numero no es primo")