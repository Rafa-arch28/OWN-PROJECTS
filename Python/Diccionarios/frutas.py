"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una 
fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el 
diccionario debe mostrar un mensaje informando de ello.
"""

p_frutas = {"platano": 1.35, "manzana": 0.80, "pera": 0.85, "naranja": 0.70}

fruta = input("Ingrese el nombre de la fruta que quiere: ").lower()

if fruta in p_frutas:
    kilos = float(input("Ingrese el número de kilos de fruta: "))
    total = kilos * p_frutas[fruta]
    print(f"El precio de {kilos} kg de {fruta} es de: ${total:.2f}")
else:
    print("No encontré la fruta :(")