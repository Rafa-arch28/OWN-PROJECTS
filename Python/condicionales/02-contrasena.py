"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario 
por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la 
guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""

contrasena = "hola1234"
contrasena_i = input("Ingrese la contrasena: ")

if contrasena_i.lower() == contrasena.lower():
    print("La contrasena coincide")
else:
    print("La contrasena no coincide")

"""
Ejercicio de condicionales simples donde uso el metodo .lower() en las dos contrasenas para que no importen las
mayusuclas y las minusculas, asi que uso condicionales y a la vez metodos de strings para hacer este
programa, me gusta mucho que ya pueda hacer este tipo de cosas con todo lo que estoy aprendiendo :)
"""