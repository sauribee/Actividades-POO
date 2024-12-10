import math as m

class TrianguloEquilatero:
    """
    Clase que representa un triángulo equilátero y permite calcular su perímetro, altura y área.
    """
    def __init__(self, lado: float) -> None:
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 3 * self.lado

    def calcular_altura(self) -> float:
        return (m.sqrt(3) / 2) * self.lado

    def calcular_area(self) -> float:
        return (m.sqrt(3) / 4) * (self.lado ** 2)

if __name__ == "__main__":
    lado = float(input("Ingrese el lado del triángulo equilátero: ")) # Se solicita que ingrese el lado del triángulo equilátero.
    triangulo = TrianguloEquilatero(lado)
    print(f"Perímetro del triángulo equilátero: {triangulo.calcular_perimetro():.2f}")
    print(f"Altura del triángulo equilátero: {triangulo.calcular_altura():.2f}")
    print(f"Área del triángulo equilátero: {triangulo.calcular_area():.2f}")