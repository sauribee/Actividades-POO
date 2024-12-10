import math as m

class Circulo:
    """
    Clase que representa un círculo y permite calcular su área y perímetro.
    """
    def __init__(self, radio: float) -> None:
        self.radio = radio

    def calcular_area(self) -> float:
        return m.pi * (self.radio ** 2)

    def calcular_perimetro(self) -> float:
        return 2 * m.pi * self.radio

class Rectangulo:
    """
    Clase que representa un rectángulo y permite calcular su área y perímetro.
    """
    def __init__(self, base: float, altura: float) -> None:    
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        return 2 * (self.base + self.altura)

class Cuadrado:
    """
    Clase que representa un cuadrado y permite calcular su área y perímetro.
    """
    def __init__(self, lado: float) -> None:
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado ** 2

    def calcular_perimetro(self) -> float:
        return 4 * self.lado

class TrianguloRectangulo:
    """
    Clase que representa un triángulo rectángulo y permite calcular su área, perímetro y determinar el tipo de triángulo que es.
    """
    def __init__(self, base: float, altura: float) -> None:
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2

    def calcular_perimetro(self) -> float:
        return self.base + self.altura + self.calcular_hipotenusa()

    def calcular_hipotenusa(self) -> float:
        return m.sqrt(self.base ** 2 + self.altura ** 2)

    def tipo_triangulo(self) -> str:
        hipotenusa = self.calcular_hipotenusa()
        if self.base == self.altura == hipotenusa:
            return "Equilátero"
        elif self.base == self.altura or self.base == hipotenusa or self.altura == hipotenusa:
            return "Isósceles"
        else:
            return "Escaleno"

def prueba_figuras_geometricas() -> None:
    radio = float(input("Ingrese el radio del círculo: ")) # Ingrese el radio del círculo.
    circulo = Circulo(radio)
    print(f"Área del círculo: {circulo.calcular_area():.2f}")
    print(f"Perímetro del círculo: {circulo.calcular_perimetro():.2f}")

    base = float(input("Ingrese la base del rectángulo: ")) # Ingrese la base del rectángulo.
    altura = float(input("Ingrese la altura del rectángulo: ")) # Ingrese la altura del rectángulo.
    rectangulo = Rectangulo(base, altura)
    print(f"Área del rectángulo: {rectangulo.calcular_area():.2f}")
    print(f"Perímetro del rectángulo: {rectangulo.calcular_perimetro():.2f}")

    lado = float(input("Ingrese el lado del cuadrado: ")) # Ingrese el lado del cuadrado.
    cuadrado = Cuadrado(lado)
    print(f"Área del cuadrado: {cuadrado.calcular_area():.2f}")
    print(f"Perímetro del cuadrado: {cuadrado.calcular_perimetro():.2f}")

    base = float(input("Ingrese la base del triángulo rectángulo: ")) # Ingrese la base del triángulo rectángulo.
    altura = float(input("Ingrese la altura del triángulo rectángulo: ")) # Ingrese la altura del triángulo rectángulo.
    triangulo = TrianguloRectangulo(base, altura)
    print(f"Área del triángulo rectángulo: {triangulo.calcular_area():.2f}")
    print(f"Perímetro del triángulo rectángulo: {triangulo.calcular_perimetro():.2f}")
    print(f"Tipo de triángulo: {triangulo.tipo_triangulo()}")
    
if __name__ == "__main__":
    prueba_figuras_geometricas()