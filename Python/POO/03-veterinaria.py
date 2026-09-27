class Mascota:
    def __init__(self, nombre = None, especie = None, edad = None, esta_vacunado = False):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.esta_vacunado = esta_vacunado

    def cumplir_anos(self):
        self.edad += 1

    def vacunar(self):
        self.esta_vacunado = True
        print("La mascota esta vacunada")

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Especie: {self.especie}")
        print(f"Estado:  {'Esta vacunado' if self.esta_vacunado else 'No esta vacunado'}") #OPERADOR TENARIO

    def __str__(self):
        return(f"Nombre: {self.nombre}\nEspecie: {self.especie}\nEdad: {self.edad}\nEstado: {'Esta vacunado' if self.esta_vacunado == True else 'No esta vacunado'}")


m1 = Mascota("rafa", "perro", 1, True)

m1.cumplir_anos()
m1.mostrar_informacion()

m1.nombre = "hola"
m1.esta_vacunado = False

m1.mostrar_informacion()