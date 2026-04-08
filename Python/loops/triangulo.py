""" Ejercicio 6
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
rectángulo como el de más abajo, de altura el número introducido.

*
**
***
****
***** """

tamano = int(input("Ingrese la altura de su triangulo: "))

for i in range (1, tamano + 1):
    print("*" * i)

""" Codigo creo que sencillo pero es de mis primeros codigos con Python, lo hice facil porque ya
sabia la sontaxis pero es que pasasr de un lenguaje tan restrictivo como C++ a uno en donde casi no hay 
reglas es un poco dificil para mi, pero es facil porque no hay cout ni nada de eso es muy facil. """