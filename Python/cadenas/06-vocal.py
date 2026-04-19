"""
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después 
muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""

frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal de la frase en minúscula: ")

frase_modificada = frase.replace(vocal, vocal.upper())

print(frase_modificada)

"""
Okey ya con esto tengo varios metodos para usar con strings, el replace esta sencillo por que es:
.replace(lo que busco, con lo que quiero reemplazar) y esta facil si pero es que estos son cosas que yo
no se asi que si se me complica un poco mas pero ya con todo esto nuevo que aprendo estoy seguro que podre
hacerlo mejor cuando necesite usar strings para algun programa :)
"""