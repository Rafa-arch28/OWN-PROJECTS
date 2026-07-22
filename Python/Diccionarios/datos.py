"""
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""

datos = {}
continuar = True

while continuar:
    clave = input("Ingrese el valor que va a poner: ")
    valor = input(f"Ingrese su {clave} porfavor: ")

    datos[clave] = valor

    print(f"Diccionario: {datos}")

    r = input("Quieres agregar otro dato? (s/n): ").lower()

    if r != "s":
        continuar = False