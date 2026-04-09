"""
Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el 
número de años, y muestre por pantalla el capital obtenido en la inversión.
"""
cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))

interes_anual = (float(input("Ingrese la taza de interes anual: "))) / 100

anos = int(input("Ingrese la cantidad de años: "))

interes_simple = (cantidad_invertir * interes_anual) * anos
capital_obtenido = cantidad_invertir * (1 + interes_anual) ** anos

print(f"La cantidad gana de intereses es de: {interes_simple:.2f}")
print(f"La capital total despues de {anos} años es de: {capital_obtenido:.2f}")

"""
En este ejercicio compare el interes simple contra el compuesto, para sacar todo esto uso los operadores
que aprendi de anteriores ejercicios. Parece raro escribir codigo asi casi sin reglas pero es mucho mas 
facil
"""
