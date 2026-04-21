"""
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta 
formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el 
grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla 
el grupo que le corresponde.
"""
nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo [M] o [H]: ")

"""
Se me habia ocurrido algo asi porque se que [] tambien sirven para agrrar caracteres en strings, no solo
para listas pero la verdad se me olvido como hacer eso asi que busque en google y la verdad si era como lo
recordaba pero a veces es mejor asegurar.
"""
primer_letra = nombre.upper()[0]

if (sexo == "M" and primer_letra < "M") or (sexo == "H" and primer_letra < "N"):
    grupo = "A"
else:
    grupo = "B"

print(f"Su grupo es: {grupo}")

"""
Este programa me ayudo mucho porque SIEMPRE batallo con los strings jajaj pero las condiciones de evaluar
la letra la verdad me sorprendio porque no sabia que se podia hacer asi de facil, yo pensaba en hacer como
que una lista con todas las letras y ahi evaluar si estaba antes de la posicion pero creo que es algo que solo
haria en c++ jajja pero lo bueno que estamos en python y aqui tooodo es mas facil. Programa un poco mas
dificl de lo habitual :)
"""