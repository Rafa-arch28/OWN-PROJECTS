"""
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el 
artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar 
por pantalla la lista de la compra y el coste total, con el siguiente formato
"""

lista = {}
total = 0
continuar = True

while continuar:
    art = input("Ingrese el articulo: ")
    precio = float(input(f"Ingrese el precio de {art}: "))

    lista[art] = precio
    total += precio

    r = input("Desea continuar agregando a la compra? (s/n): ")

    if r != "s":
        continuar = False

for articulo, costo in lista.items():
    print(f"{articulo}               {costo}")

print(f"Total               {total}")
