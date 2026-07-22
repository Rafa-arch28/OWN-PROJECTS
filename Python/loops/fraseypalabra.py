"""
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla 
el número de veces que aparece la letra en la frase.
"""

frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

c_letra = 0

for letras in frase:
    if letras == letra:
        c_letra += 1

print(f"Las veces que la letra salio en la frase fueron de: {c_letra}")