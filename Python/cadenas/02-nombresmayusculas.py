"""
Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla 
el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras 
mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""

nombre = input("Ingrese su nombre completo: ")

# Estas lineas eran para ver si tenia razon con los metodos .upper() y esos. 
"""
print(nombre.upper())
print(nombre.lower())
print(nombre.title())
"""
# Tambien pense en usar .capitalize() pero solo pondria la primer leta en mayusculas
print(f"{nombre.upper()}\n{nombre.lower()}\n{nombre.title()}") # Me da un poco de miedo lo poco que se entiende

"""
En este ejercicio practique con los metodos para alterar los strings, estan faciles de recordar de hecho pero
tambien se me olvidaron los parentesis al principio pero todo bien, del metodo .title() no me acordaba
mucho pero con una busqueda rapida en google me llevo mas conocimientos.
"""