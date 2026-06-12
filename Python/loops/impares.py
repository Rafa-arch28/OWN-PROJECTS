"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares 
desde 1 hasta ese número separados por comas.
"""

numero = int(input("Ingrese el numero impar: "))

for i in range(1, numero + 1):
    if i % 2 == 1:
        print(i, end= ", ")

"""
Este programa es de lo mas dificiles que he hecho jajajaj en c++ es mucho mas logico pero aqui python no sabe como
recorrer un numero entero, pero esta facil solo tengo que aprender lo de range(1, hasta esto) y pues ya esta super facil
pero VOLVEMOS A DARLE A LA PROGRAMACION, tengo que volverme nivel senior en dos meses jajajaj es broma pero si quiero
aprender mucho mas asi que si. tambien aprendi lo de end, pero eso es bastante logico :)
"""