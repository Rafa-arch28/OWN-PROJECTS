"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
"""

palabra = input("Ingrese la palabra: ")

vocales = ["a","e","i","o","u"]

for vocal in vocales:
    veces_vocal = palabra.count(vocal)

    print(f"La vocal {vocal} aparece {veces_vocal} veces")