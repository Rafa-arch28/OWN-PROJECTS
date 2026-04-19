"""
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por 
comas, y muestre por pantalla cada uno de los productos en una línea distinta.
"""

compras = input("Ingrese su lista de compras separada por comas: ")

lista = compras.split(',')

print("PRODUCTOS: ")

for producto in lista:
    print(producto)

"""
WOOOWWW con este ejercicio la verdad si me senti muy pro porque usar el for sin tener que determinar el
rango es como wow, ya estoy listo para listas y tuplas y diccionarios. Es lo mismo que los ultimos ejercicios
pero ahora usando for para sacar esos elementos en lineas distintas sin muchos print :)
"""