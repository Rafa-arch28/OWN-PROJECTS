"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás 
desde ese número hasta cero separados por comas.
"""

num = int(input("Ingrese un numero entero positivo: "))

# retiro lo dicho de la funcion range, la odio que esta aberrosidad
for i in range(num, -1, -1):
    print(i, end= ", ")

# ENCONTRE UNA FORMA MUUUCHO MAS FACIL
for i in reversed(range(num + 1)):
    print(i)
# tenia dudas del porque cuando lo ponia normal como que se saltaba el cero, pero es pq iniciaba en 1 y se pasaba el 0
#entonces por eso :) 