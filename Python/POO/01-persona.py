class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        self.nombre = nombre;
        self.edad = edad;
        self.dni = dni;

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre is not None and len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre

    @property
    def edad(self):
        return self._edad  # Se usa el _ antes de la variable para indicar que es la variable donde se pondra el valor final

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad is not None and nueva_edad > 0:
            self._edad = nueva_edad;
        else:
            print("La edad no puede ser negativa !!!")

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, nuevo_dni):
        if nuevo_dni is not None and len(nuevo_dni) > 0:
            self._dni = nuevo_dni
        else:
            print("Su DNI no puede ser negativo")

    def mostrar(self):
        print(f"Nombre: {self.nombre}  Edad: {self.edad}  DNI: {self.dni}")

    def esMayorDeEdad(self):
        if self.edad >= 18:
            print("Es mayor de edad")
            return True
        else:
            print("No es mayor de edad")
            return False

    def __str__(self):
        return f"Nombre: {self.nombre}  Edad: {self.edad}  DNI: {self.dni}"


nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
dni = input("Ingrese su dni: ")

nuevo = Persona(nombre, edad, dni)

nuevo.esMayorDeEdad()

nuevo.mostrar()