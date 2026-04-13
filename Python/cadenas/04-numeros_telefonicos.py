"""
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el 
código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa
que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el 
prefijo y la extensión.
"""

numero_telefonico = input("Formato: +34-SU NUMERO-EXTENSION. Teniendo en cuenta esto, ingrese su numero: ")

# USO UN NUEVO METODO: .split()
partes = numero_telefonico.split('-')

#otra forma de hacerlo es contando caracteres: 
numero_solo = numero_telefonico[4:-3]
# Este metodo funciona ya que la extension tiene siempre 4 caracteres y la extension siempre son los ultimos
# 3 caracteres, asi que se puede como que recortar el string. Aun asi prefiero split porque ya estan los - puestos

# Se usa [1] dentro de split porque es la posicion del centro, las listas inician en 0, no en 1
print(f"El numero de telefono es: {partes[1]}")

"""
Aprendi el nuevo metodo de split, que se usa para dividir en partes strings. Si  lo mostraramos se veria como
una lista con cada palabra separada por el divisor que en este caso es '-', esta muy facil con eso de los 
divisores :)

La otra opcion no creo que sirva mmucho por ejemplo si llegara a produccion porque seria solo para que el
prefijo tenga esos caracteres en concreto y que la extension iniciara siempre en el caracter -3

Con todo eso dicho, aprendi muucho mucho de strings, asi que todo good >:)
"""