"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""

palabra = input("Ingrese su frase: ")

palindromo = palabra[::-1]

if palabra == palindromo:
    print("La palara es un palindromo")
else:
    print("No es palindromo")

palabra = input("Ingrese su frase: ")

original = list(palabra)
reverseada = original.copy()
reverseada.reverse()

if original == reverseada:
    print("Palindromo")
else:
    print("No palindromo")
