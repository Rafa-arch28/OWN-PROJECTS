"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y 
Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las 
asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""

n = int(input("Cuantas materias son?: "))

materias = []
calif_materias = []
reprobadas = []

for i in range(n):
    n_materia = input("Ingrese el nombre de la materia: ")
    materias.append(n_materia)
    c_materia = float(input("Ingrese la calificacion de la materia: "))
    calif_materias.append(c_materia)

for i in range(n):
    if calif_materias[i] >= 70:
        reprobadas.append(materias[i])

for materia in reprobadas:
    print(f"Tienes que repetir {materia} por que reprobaste")