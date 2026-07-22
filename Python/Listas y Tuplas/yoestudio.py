"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la 
muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
"""

n = int(input("Cuantas materias son?: "))

materias = []

for i in range(n):
    n_materia = input("Ingrese el nombre de la materia: ")
    materias.append(n_materia)

for materia in materias:
    print(f"Yo estudio {materia}")