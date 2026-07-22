"""
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono 
es <teléfono>.
"""

datos = {}

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
direccion = input("Ingrese su direccion: ")
telefono = input("Ingrese su telefono: ")

datos["nombre"] = nombre
datos["edad"] = edad
datos["direccion"] = direccion
datos["telefono"] = telefono

print(f"{datos['nombre']} tiene {datos['edad']} anos, vive en {datos['direccion']} y su numero de telefono es {datos['telefono']}")