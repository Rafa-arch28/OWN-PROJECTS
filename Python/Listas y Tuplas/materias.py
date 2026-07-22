"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
"""

n_materias = int(input("Ingrese el numero de materias que quiere guardar: "))

materias = []

for i in range(n_materias):
    nue_materias = input("Ingrese el nombre de la materia: ")
    materias.append(nue_materias)

for materia in materias:
    print(materia)