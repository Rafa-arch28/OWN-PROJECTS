"""
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato 
dd de <mes> de aaaa donde <mes> es el nombre del mes.
"""
meses = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]

fecha = input("Ingrese la fecha en formato dd/mm/aaaa: ")

partes = fecha.split("/")

dia = partes[0]
mes = int(partes[1])
ano = partes[2]

nombre_mes = meses[mes - 1]

print(f"{dia} de {nombre_mes} de {ano}")