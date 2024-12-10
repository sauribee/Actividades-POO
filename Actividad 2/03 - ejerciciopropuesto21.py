import math as m

class TrianguloRectangulo:
    """
    Clase que representa un triángulo y permite calcular su perímetro, semiperímetro y área a partir de sus lados.
    """
    def __init__(self, lado1: float, lado2: float, lado3: float) -> None:
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self) -> float:
        return self.lado1 + self.lado2 + self.lado3

    def calcular_semiperimetro(self) -> float:
        return self.calcular_perimetro() / 2

    def calcular_area(self) -> float:
        s = self.calcular_semiperimetro()
        return m.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

if __name__ == "__main__":
    lado1 = float(input("Ingrese el lado 1 del triángulo: ")) # Se solicita que ingrese el lado 1 del triángulo.
    lado2 = float(input("Ingrese el lado 2 del triángulo: ")) # Se solicita que ingrese el lado 2 del triángulo.
    lado3 = float(input("Ingrese el lado 3 del triángulo: ")) # Se solicita que ingrese el lado 3 del triángulo.
    triangulo = TrianguloRectangulo(lado1, lado2, lado3)
    print(f"Perímetro del triángulo: {triangulo.calcular_perimetro():.2f}")
    print(f"Semiperímetro del triángulo: {triangulo.calcular_semiperimetro():.2f}")
    print(f"Área del triángulo: {triangulo.calcular_area():.2f}")