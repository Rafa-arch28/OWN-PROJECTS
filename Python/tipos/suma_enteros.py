"""
Ejercicio 6
Escribir un programa que lea un entero positivo, n, introducido por el usuario y des-
pués muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los
n primeros enteros positivos puede ser calculada de la siguiente forma:

suma = (n x (n + 1)) / 2
"""
numero = int(input("Ingrese el numero entero: "))
suma = int((numero * (numero + 1)) / 2)

print(f"La suma de los enteros desde 1 hasta el {numero} es: {suma}")

"""
Estaba investigando de esta formula y descubri que se llama "Formula de Gauss", es interesamte y me 
gustan mucho los ejercicios que son mas de matematicas y logica que de pura sintaxis, se me hace muy 
divertido.
Un comentario a parte es que esta formula es mucho mas eficiente y sencilla que usar un bucle for.
"""