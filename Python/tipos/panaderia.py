"""
Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el 
programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser 
fresca y el coste final total.
"""

# EUROS
PAN_FRESCO = 3.49
# Este es un descuento del 60%
DESCUENTO_NO_FRESCO = 0.6

barras_no_frescas = int(input("Ingrese el numero de pan que no es del dia: "))

dinero_descontado = PAN_FRESCO * DESCUENTO_NO_FRESCO

precio_final_barra = PAN_FRESCO - dinero_descontado

precio_total = barras_no_frescas * precio_final_barra

print(f"El precio habitual de una barra de pan es de: {PAN_FRESCO}, El descuento por no ser fresca es de: {dinero_descontado:.2f}, EL precio total es de: {precio_total:.2f}")

"""
Entendí que el descuento es el dinero que se LE QUITA al precio original.
Si el descuento es del 60%, el precio final es el 40%.
También aprendí que si cambio el nombre de una variable arriba, debo
cambiarlo en todos los lugares donde la use (como en el print). Este es mi ultimo
ejercicio de tipos, seguimos con cadenas.
"""