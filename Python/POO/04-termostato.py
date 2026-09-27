class Termostato:
    def __init__(self, temperatura_actual = 20, temperatura_objetivo = None):
        self.temperatura_actual = temperatura_actual
        self.temperatura_objetivo = temperatura_objetivo

    def definir_objetivo(self):
        nueva_temperatura = float(input("Ingrese una temperatura Objetivo (entre 15.0 y 30.0): "))
        self.temperatura_objetivo = nueva_temperatura if nueva_temperatura >= 15 or nueva_temperatura <= 30 else "ESA TEMPERATURA NO ESTA PERMITIDA, VUELVA A INTENTARLO"

    def regular(self):
        while self.temperatura_actual != self.temperatura_objetivo:
            if self.temperatura_actual < self.temperatura_objetivo:
                pass