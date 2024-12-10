class ComparadorNumerosEnteros:
    """
    Clase que permite comparar dos números enteros y mostrar cuál es mayor, menor o si son iguales.
    """    
    def __init__(self, numero_A: int, numero_B: int) -> None:
        self.numero_A = numero_A
        self.numero_B = numero_B

    def comparar_numeros(self) -> str:
        if self.numero_A > self.numero_B:
            return f"{self.numero_A} es mayor que {self.numero_B}"
        elif self.numero_A == self.numero_B:
            return f"{self.numero_A} es igual a {self.numero_B}"
        else:
            return f"{self.numero_A} es menor que {self.numero_B}"

    def mostrar_resultado(self) -> None:
        print(self.comparar_numeros())

if __name__ == "__main__":
    numero_A = int(input("Ingrese el número A: ")) # Se solicita que ingrese el número A.
    numero_B = int(input("Ingrese el número B: ")) # Se solicita que ingrese el número B.
    comparador = ComparadorNumerosEnteros(numero_A, numero_B)
    comparador.mostrar_resultado()