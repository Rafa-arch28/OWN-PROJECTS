"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
rectángulo como el de más abajo.
"""

filas = int(input("Ingrese un numero entero positivo: "))

for i in range(1, filas + 1):
    for j in range(2 * i - 1, 0, -2):
        print(j, end="")
    print()