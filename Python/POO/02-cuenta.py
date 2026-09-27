class Cuenta:
    def __init__(self, titular, cantidad=None): # SI quieres que un atributo no sea obligatorio solo asignale un valor
        self.titular = titular
        self.cantidad = cantidad

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, nuevo_titular):
        if nuevo_titular is not None and len(nuevo_titular) > 0:
            self._titular = nuevo_titular
        else:
            print("El nombre esta vacio")

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        if nueva_cantidad is not None and nueva_cantidad > 0:
            self._cantidad = nueva_cantidad
        else:
            print("La cantidad esta vacia o es negativa")

    def ingresar(self):
        opc = input("Desea ingresar una cantidad? S/n : ").upper()
        if opc == "S":
            cantidad = float(input("Ingrese la cantidad: "))
            self.cantidad = cantidad
        else:
            print("Okey, no se hara nada")

    def retirar(self):
        opc = input("Desea retirar dinero? S/n : ").upper()
        if opc == "S":
            cantidad_retirar = float(input("Ingrese la cantidad a retirar: "))
            self.cantidad -= cantidad_retirar;
        else:
            print("Okey, no se hara nada ")

    def mostrar(self):
        print(f"Titular: {self.titular}  Cantidad: {self.cantidad}")

    def __str__(self):
        return f"Titular: {self.titular}  Cantidad: {self.cantidad}"



nombre = input("Ingrese su nombre: ")
p1 = Cuenta(nombre)

p1.ingresar()
p1.mostrar()

p1.retirar()
p1.mostrar()