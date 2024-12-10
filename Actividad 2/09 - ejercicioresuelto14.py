class Departamento:
    """
    Clase que representa un departamento de una empresa y permite calcular el salario final de los vendedores del departamento a partir de sus ventas y salario, y mostrar los salarios finales de los vendedores del departamento.
    """
    def __init__(self, ventas_departamento: float, salario: float) -> None:
        self.ventas_departamento = ventas_departamento
        self.salario = salario

    def calcular_salario_final(self, total_ventas: float) -> float:
        porcentaje_ventas = 0.33 * total_ventas
        if self.ventas_departamento > porcentaje_ventas:
            salario_final = self.salario + 0.2 * self.salario
        else:
            salario_final = self.salario
        return salario_final

class Empresa(Departamento):
    """
    Clase que representa una empresa y permite calcular el salario final de los vendedores de tres departamentos a partir de sus ventas y salario, y mostrar los salarios finales de los vendedores de los tres departamentos.
    """
    def __init__(self, ventas_departamento1: float, ventas_departamento2: float, ventas_departamento3: float, salario: float) -> None:    
        self.departamento1 = Departamento(ventas_departamento1, salario)
        self.departamento2 = Departamento(ventas_departamento2, salario)
        self.departamento3 = Departamento(ventas_departamento3, salario)
        self.total_ventas = ventas_departamento1 + ventas_departamento2 + ventas_departamento3

    def mostrar_salarios(self) -> None:
        salario_departamento1 = self.departamento1.calcular_salario_final(self.total_ventas)
        salario_departamento2 = self.departamento2.calcular_salario_final(self.total_ventas)
        salario_departamento3 = self.departamento3.calcular_salario_final(self.total_ventas)
        print(f"Salario de los vendedores del departamento 1: ${salario_departamento1:.2f}")
        print(f"Salario de los vendedores del departamento 2: ${salario_departamento2:.2f}")
        print(f"Salario de los vendedores del departamento 3: ${salario_departamento3:.2f}")

if __name__ == "__main__":
    ventas_departamento1 = float(input("Ingrese las ventas del departamento 1: ")) # Se solicita que ingrese las ventas del departamento 1.
    ventas_departamento2 = float(input("Ingrese las ventas del departamento 2: ")) # Se solicita que ingrese las ventas del departamento 2.
    ventas_departamento3 = float(input("Ingrese las ventas del departamento 3: ")) # Se solicita que ingrese las ventas del departamento 3.
    salario = float(input("Ingrese el salario base de los vendedores: ")) # Se solicita que ingrese el salario base de los vendedores.
    empresa = Empresa(ventas_departamento1, ventas_departamento2, ventas_departamento3, salario)
    empresa.mostrar_salarios()