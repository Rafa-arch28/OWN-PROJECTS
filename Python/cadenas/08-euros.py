"""
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y 
muestre por pantalla el número de euros y el número de céntimos del precio introducido.
"""
euros = input("Ingrese la cantidad de euros con dos decimales: ")

partes = euros.split('.')

print(f"Euros: {partes[0]}, Centimos: {partes[1]}")

"""
Aqui uso la misma logica que el ejercicio anterior, la verdad ya cuando sabes mas de los metodos es super
facil resolver este tipo de problemas, me alegra mucho que haya podido aprender mas :)
"""