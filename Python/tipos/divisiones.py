"""
Ejercicio 8: Cociente y Residuo
Este programa separa una división en sus dos partes enteras:
cuántas veces cabe y cuánto sobra.
"""

num1 = int(input("Ingrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))

cociente = num1 // num2 # El operador // busca cuantas veces cabe el divisor en el dividendo
residuo = num1 % num2 # Agarra el numero que sobra entre el divisor y el dividendo

print(f"{num1} entre {num2} da un cociente de {cociente:.2f} y un residuo de {residuo}")

""" Con este ejercicio entendi lo que es el modulo, el operador para residuos de divison '%'. Es 
lo mismo que se usa para ver si un numero es par o impar (n % 2 == 0), es mucho mas facil que usar decimales """
