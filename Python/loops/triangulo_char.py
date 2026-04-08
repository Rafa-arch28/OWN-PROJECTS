""" Ejercicio 9
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta. """

contrasena = "daraf2030"

while True: 
    contrasena_ingresada = input("Ingrese la contrasena: ")

    if contrasena_ingresada == contrasena:
        print("Contrasena correcta")
        break
    else:
        print("Contrasena incorrecta. Intenta de nuevo")

""" Sencillooo, lo que cambia de C++ es el While True o sea un bucle infinito sin tener que usar
banderas, solo el break y ya. Fuera de eso esta bien pero me inquieta la variable dentro del while """