class Esfera:
    """
    Clase que representa una esfera y permite comparar tres esferas para encontrar cuál es la esfera de mayor peso.
    """
    def __init__(self, peso: float, nombre: str) -> None:
        self.peso = peso
        self.nombre = nombre

class ComparadorEsferas(Esfera):
    """
    Clase que permite comparar tres esferas para encontrar cuál es de mayor peso.
    """
    def __init__(self, esferaA: Esfera, esferaB: Esfera, esferaC: Esfera) -> None:
        self.esferaA = esferaA
        self.esferaB = esferaB
        self.esferaC = esferaC

    def encontrar_esfera_mayor(self) -> Esfera:
        if self.esferaA.peso > self.esferaB.peso and self.esferaA.peso > self.esferaC.peso:
            mayor = self.esferaA
        elif self.esferaB.peso > self.esferaA.peso and self.esferaB.peso > self.esferaC.peso:
            mayor = self.esferaB
        else:
            mayor = self.esferaC
        return mayor

    def mostrar_esfera_mayor(self) -> None:    
        mayor = self.encontrar_esfera_mayor()
        print(f"La esfera de mayor peso es: {mayor.nombre} con un peso de {mayor.peso}")

if __name__ == "__main__":
    pesoA = float(input("Ingrese el peso de la esfera A: ")) # Ingrese el peso de la esfera A.
    pesoB = float(input("Ingrese el peso de la esfera B: ")) # Ingrese el peso de la esfera B.
    pesoC = float(input("Ingrese el peso de la esfera C: ")) # Ingrese el peso de la esfera C.
    esferaA = Esfera(pesoA, "A")
    esferaB = Esfera(pesoB, "B")
    esferaC = Esfera(pesoC, "C")
    comparador = ComparadorEsferas(esferaA, esferaB, esferaC)
    comparador.mostrar_esfera_mayor()