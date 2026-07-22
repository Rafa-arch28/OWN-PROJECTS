"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""
CONTRASENA = "DARIO"

while True:
    contrasena_u = input("Ingrese la contrasena: ")
    if(contrasena_u == CONTRASENA):
        break
