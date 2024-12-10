class Esfera:
    """
    Clase que representa una esfera y permite comparar cuatro esferas para encontrar cuál es diferente y si es de mayor o menor peso.
    """
    def __init__(self, peso: float, nombre: str) -> None:
        self.peso = peso
        self.nombre = nombre

class ComparadorEsferas(Esfera):
    """
    Clase que permite comparar cuatro esferas para encontrar cuál es diferente y si es de mayor o menor peso.
    """
    def __init__(self, esferaA: Esfera, esferaB: Esfera, esferaC: Esfera, esferaD: Esfera) -> None:             
        self.esferaA = esferaA
        self.esferaB = esferaB
        self.esferaC = esferaC
        self.esferaD = esferaD

    def encontrar_esfera_diferente(self) -> Esfera:
        if self.esferaA.peso == self.esferaB.peso == self.esferaC.peso:
            esfera_diferente = self.esferaD
        elif self.esferaA.peso == self.esferaB.peso == self.esferaD.peso:
            esfera_diferente = self.esferaC
        elif self.esferaA.peso == self.esferaC.peso == self.esferaD.peso:
            esfera_diferente = self.esferaB
        else:
            esfera_diferente = self.esferaA
        return esfera_diferente

    def mostrar_esfera_diferente(self) -> None:
        esfera_diferente = self.encontrar_esfera_diferente()
        if esfera_diferente.peso > self.esferaA.peso:
            print(f"La esfera {esfera_diferente.nombre} es la diferente y es de mayor peso.")
        else:
            print(f"La esfera {esfera_diferente.nombre} es la diferente y es de menor peso.")

if __name__ == "__main__":
    pesoA = float(input("Ingrese el peso de la esfera A: ")) # Ingrese el peso de la esfera A.
    pesoB = float(input("Ingrese el peso de la esfera B: ")) # Ingrese el peso de la esfera B.
    pesoC = float(input("Ingrese el peso de la esfera C: ")) # Ingrese el peso de la esfera C.
    pesoD = float(input("Ingrese el peso de la esfera D: ")) # Ingrese el peso de la esfera D.
    esferaA = Esfera(pesoA, "A")
    esferaB = Esfera(pesoB, "B")
    esferaC = Esfera(pesoC, "C")
    esferaD = Esfera(pesoD, "D")
    comparador = ComparadorEsferas(esferaA, esferaB, esferaC, esferaD)
    comparador.mostrar_esfera_diferente()