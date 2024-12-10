import math as m

class EcuacionSegundoGrado:
    """
    Clase que representa una ecuación de segundo grado ax^2+bx+c=0 y permite calcular sus soluciones reales.
    """
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

    def calcular_discriminante(self) -> float:
        return self.b ** 2 - 4 * self.a * self.c

    def calcular_soluciones(self) -> tuple:
        discriminante = self.calcular_discriminante()
        if discriminante < 0:
            return None, None
        else:
            x1 = (-self.b + m.sqrt(discriminante)) / (2 * self.a)
            x2 = (-self.b - m.sqrt(discriminante)) / (2 * self.a)
            return x1, x2

    def mostrar_soluciones(self) -> None:
        x1, x2 = self.calcular_soluciones()
        if x1 is None and x2 is None:
            print("La ecuación no tiene soluciones reales.")
        else:
            print(f"Las soluciones de la ecuación son: x1 = {x1:.2f}, x2 = {x2:.2f}")

if __name__ == "__main__":
    a = float(input("Ingrese el valor del coeficiente A: ")) # Ingrese el valor del coeficiente a.
    b = float(input("Ingrese el valor del coeficiente B: ")) # Ingrese el valor del coeficiente b.
    c = float(input("Ingrese el valor del coeficiente C: ")) # Ingrese el valor del coeficiente c.
    ecuacion = EcuacionSegundoGrado(a, b, c)
    ecuacion.mostrar_soluciones()