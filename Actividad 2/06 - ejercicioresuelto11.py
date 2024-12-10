class ComparadorNumerosEnteros:
    """
    Clase que permite comparar tres números enteros y mostrar cuál es mayor de los tres.
    """
    def __init__(self, numero1: int, numero2: int, numero3: int) -> None:    
        self.numero1 = numero1
        self.numero2 = numero2
        self.numero3 = numero3

    def encontrar_mayor_entero(self) -> int:
        if self.numero1 > self.numero2 and self.numero1 > self.numero3:
            mayor = self.numero1
        elif self.numero2 > self.numero1 and self.numero2 > self.numero3:
            mayor = self.numero2
        else:
            mayor = self.numero3
        return mayor

    def mostrar_mayor_entero(self) -> None:
        mayor_entero = self.encontrar_mayor_entero()
        print(f"El valor mayor entre: {self.numero1}, {self.numero2} y {self.numero3} es: {mayor_entero}")

if __name__ == "__main__":
    numero1 = int(input("Ingrese el primer número: ")) # Se solicita que ingrese el primer número.
    numero2 = int(input("Ingrese el segundo número: ")) # Se solicita que ingrese el segundo número.
    numero3 = int(input("Ingrese el tercer número: ")) # Se solicita que ingrese el tercer número.
    comparador = ComparadorNumerosEnteros(numero1, numero2, numero3)
    comparador.mostrar_mayor_entero()