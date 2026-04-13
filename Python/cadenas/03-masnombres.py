"""
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo 
introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en 
mayúsculas y <n> es el número de letras que tienen el nombre.
"""
nombre = input("Ingrese su nombre: ")
longitud = len(nombre.replace(" ", "")) # Primera vez usando len y el metodo replace para omitir los espacios

# amo los f-strings
print(f"{nombre.upper()} tiene {longitud} letras")

"""
Este ejercicio me gusto la verdad porque es nuevo para mi el metdo len y es interesante que sepa cuantos
carcteres hay en un string. Lo supe investigando como siempre, a veces me siento mal porque no me esfuerzo
pero cmom voy a hacer algo cuando ni siquiera se los metodos para hacerlo jaja. Te amo Python <3
"""