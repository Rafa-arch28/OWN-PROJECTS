"""
Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance 
final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero 
depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y 
mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
Redondear cada cantidad a dos decimales.
"""

INTERES = 0.04

dinero_depositado = float(input("Ingrese el dinero depositado en la cuenta: "))

ahorro1 = dinero_depositado * (1 + INTERES) # No se puede multiplicar solo por 0.4 porque se pierde la cantidad inicial
ahorro2 = ahorro1 * (1 + INTERES) # Lo mismo en esta y la siguiente linea, es como si omitieras el primer 100%
ahorro3 = ahorro2 * (1 + INTERES)

print(f"El dinero en el ano 1: {ahorro1:.2f}")
print(f"El dinero en el ano 2: {ahorro2:.2f}")
print(f"El dinero en el ano 3: {ahorro3:.2f}")

"""
En este ejercicio me centre mas en la logica de los porcentajes ya que a veces me confundo mucho con
los 0 en los porcentajes, por ejemplo: Cuando es un porcentaje menor al 10% pasa de ser 0.1 a agregarse
un 0 despues del punto. Es un poco confuso pero llego a entenderlo.
Tambien el agregado del 1 a la taza del interes para no empezar borrando la cantidad inicial, creo que
para simplificar podria iniciar con la constante INTERES = 1.04 pero no se, creo que en programas mas grandes
eso no seria buena practica asi que lo dejare asi.
"""
