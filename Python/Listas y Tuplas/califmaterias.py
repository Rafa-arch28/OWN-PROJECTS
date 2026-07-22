"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, 
y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada 
una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
"""

n = int(input("Cuantas materias son?: "))

materias = []
calif_materias = []

for i in range(n):
    n_materia = input("Ingrese el nombre de la materia: ")
    materias.append(n_materia)
    c_materia = float(input("Ingrese la calificacion de la materia: "))
    calif_materias.append(c_materia)

for i in range(n):
    print(f"En {materias[i]} has sacado {calif_materias[i]} de calificacion")