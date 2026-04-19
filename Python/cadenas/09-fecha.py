"""
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por 
pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o 
el mes se introduzcan con un solo carácter.
"""

fecha = input("Ingrese la fecha en formato dd/mm/aaaa: ")

partes = fecha.split('/')

print(f"Dia: {partes[0]}, Mes: {partes[1]}, Ano: {partes[2]}")

"""
Es lo mismo que los ultimos dos ejercicios y de verdad me alegra mucho ya poder entender esta logica, es
muy sencilla ya cuando llevas tiempo aprendiendo :)
"""