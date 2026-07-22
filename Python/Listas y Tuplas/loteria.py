"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""

numeros_g = []

nlot = int(input("Ingrese el total de numeros ganadores: "))

for i in range(nlot):
    nums = int(input("Ingrese los numeros ganadores: "))
    numeros_g.append(nums)

numeros_g.sort()

print(numeros_g)
