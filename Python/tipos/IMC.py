"""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa 
corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> 
donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
"""

masa = float(input("Ingrese su masa en Kilogramos: "))
altura = float(input("Ingrese su altura en Metros: "))

imc = masa / (altura ** 2 )

print(f"Tu indice de masa corporal es de: {imc:.2f}")

"""
Este programa creo que hasta a mi me seria util porque casi siempre me pregunto si ando bien de peso o no,
ademas de eso sentia que el resultado estaba muy feo porque tenia demasiados decimales. Buscando un poco
vi que habia un metodo para reducirlos en los f-strings y es :.2f o el numero que quieras que salgan, es
util muy util.
"""