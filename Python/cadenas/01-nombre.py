"""
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima 
por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""

nombre = input("Ingrese su nombre: ")
repeticiones = int(input("Ingrese un numero entero: "))

# version tradicional con for
for k in range (0, repeticiones):
    print(nombre)

# print(f"{nombre * repeticiones}\n") esta es la version anterior
print((nombre + "\n") * repeticiones)

""" Mi primer programa usando strings como dato en una variable, ya sabia que python agarraba como
string los datos no especificados pero aun asi es bueno estar repasando todo esto. Aprendi tambien el
metodo que tamin existe en c++ que es \n y esta chido porque es versatil pero se tienen que hacer cosas
diferentes cosas pero esta sencillo solo es cuestion de memorizarlo :). Ahi deje mi intento de antes que 
no funciono pero sirve de ayuda"""