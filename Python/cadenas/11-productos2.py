"""
Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por 
pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 
2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
"""
nombre = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio unitario del producto: "))
unidades = int(input("Ingrese el numero de unidades: "))

coste_total = precio * unidades

print(f"{nombre}: {precio:09.2f} euros - {unidades:03d} unidades - Total: {coste_total:011.2f} euros")

"""
Este es el ejercicio final de todos los de la lista de ejercicios de cadenas, tristemente es de formateo
de strings y la verdad no es muy dificil de aprender pero es que porque usarias una f para decimales y una
de para enterooooss o sea bueno ya que. Yo ya habia usado el metodo .2f para reducir decimales a dos, pero 
al agregar al inicio 09 lo que hace es que llena los espacios restantes con 0s en un total de 9 digitos, ya
contando decimales, es lo que hace ese metodo. el 03d lo que hace es que llena los espacios SOLO de los 
enteros con 0s y ya es todo :)
"""