""" Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde. """

# Aqui van los dos input necesarios
horas_trabajadas = int(input("Ingrese el numero de horas trabajadas: "))
pago_hora = float(input("Ingrese el pago por hora: "))

#Aqui hago elcalculo del pago
paga_correspondiente = (horas_trabajadas * pago_hora)

print(f"El pago por sus horas trabajadas es de: {paga_correspondiente}")

""" Este ejercicio es el que mas me a servido. En python todo lo que viene de un input es un
string, para saber mas de esto imaginate que en el input de por ejemplo numero pones 5 y despues esa
variable la multiplicas por 2 (numero * 2), si no convirtieras antes a int saldria el 5 repetido 
2 veces por que es lo que hace python y es lo que hice en el ejercicio del triangulo de *

Este ejercicio me sirvio para aprender mas de los tipos de datos y como convertirlos desde un inicio
en el input. """