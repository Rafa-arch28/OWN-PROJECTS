"""
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla 
otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
"""

correo = input("Ingrese su correo: ")

"""
Lo que hace split es devolver una lista con los dos elementos separados, entonces no puedo reemplazar
directamente con .replace pero si puedo agarrar la primera parte antes del @ y sumarle la nueva extension
"""
partes = correo.split('@')
nuevo_correo = partes[0] + "@ceu.es"

print(nuevo_correo)