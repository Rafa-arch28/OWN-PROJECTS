"""
Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la 
frase invertida.
"""

frase = input("Ingrese su frase: ")
invertido = frase[::-1]

print(invertido)

"""
Bueno estos ejercicios creo que son los que mas se me complican de todos los lenguajes de programacion,
los strings para mi son como un enemigo porque los metodos para lidiar con ellos son un poco
extranos para mi y la verdad soy mas de numeros pero equis. Solo busque en google como hacerlo y para
no solo hacerlo por asi tambien busque el como funciona.
La sintaxis completa del [::-1] es: string[start:stop:step], cuando dejas solo start y stop python asume
que es toda la cadena, el -1 es para que inicie desde el final ya que el string 0 es el inicio, por lo que
-1 es el final y asi sucesivamente :)
"""