"""
Ejercicio 10
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo 
y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos 
y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso 
total del paquete que será enviado.
"""

# No hay constantes en Pytuon como en C++ pero se usan mayusculas para resaltarlas y que no sean alteradas
PESO_PAYASO = 112
PESO_MUNECA = 75

print(type(PESO_PAYASO)) # Esto lo uso para verificar que Python no lo tome como un string jaja

payasos = int(input("Ingrese la cantidad de payasos: "))
munecas = int(input("Ingrese la cantidad de munecas: "))

peso_totalg =  (payasos * PESO_PAYASO) + (munecas * PESO_MUNECA)
peso_totalkg = peso_totalg / 1000

print(f"El peso total del paquete es de: {peso_totalkg:.2f}")

"""
En este ejercicio mi primer pensamiento fue usar una constante, antes de investigar me puse a 
experimentar si habia algo como const o asi pero no existe, entonces ya me meti a Google y descubri
que no existian en python pero que se usaban mayusculas para senanarlas. Puse mayusculas y
se pusieron de otro color entonces supongo que es verdad. Ademas de eso estaba practicando en la conversion
de unidades.

Una cosa extra es que se ne hizo posible que Python agarrara el valor de las constantes como un string
por experiencias pasadas jajaja, para verificarlo primero intente con un print con la variable y un .type
pero no existia, deje el print y dentro de el escribi type y vs code me recomendo type y la use con ()
dentro de ellos estaba la variable y en el output salio <class: int> entonces si agarra los datos directos
de una variable. Otra enseñanza que me llevo.
"""