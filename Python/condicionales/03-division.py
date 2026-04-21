"""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error.
"""

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

if num1 == 0 or num2 == 0:
    print("Error, no se puede dividir entre cero :)")
else:
    division = num1 / num2
    print(f"Resultado: {division}")

"""
Este programa estuvo medio facil porque pues es solo verificar que uno de los dos no sea 0 con el 
operador logico or, la verdad estuvo a punto de poner || como en c++ peo pues ya paso jajajaja, solo es
cuidar las condicionales y me encanta que no haya problema con definir variables en python dentro
de condicionales o ciclos, es increible :)
"""