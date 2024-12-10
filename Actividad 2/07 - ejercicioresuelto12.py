class SalarioTrabajador:
    """
    Clase que permite calcular el salario de un trabajador a partir de las horas trabajadas y el valor de la hora, y mostrar la información del trabajador con su salario.
    """    
    def __init__(self, nombre_trabajador: str, horas_trabajadas: int, valor_hora: float) -> None:
        self.nombre_trabajador = nombre_trabajador
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora

    def calcular_salario(self) -> float:
        if self.horas_trabajadas > 40:
            horas_extras = self.horas_trabajadas - 40
            if horas_extras > 8:
                horas_extras_excedentes = horas_extras - 8
                salario_trabajador = 40 * self.valor_hora + 16 * self.valor_hora + horas_extras_excedentes * 3 * self.valor_hora
            else:
                salario_trabajador = 40 * self.valor_hora + horas_extras * 2 * self.valor_hora
        else:
            salario_trabajador = self.horas_trabajadas * self.valor_hora
        return salario_trabajador

    def mostrar_salario(self) -> None:
        salario = self.calcular_salario()
        print(f"El trabajador {self.nombre_trabajador} devengó: ${salario:.2f}")

if __name__ == "__main__":
    nombre_trabajador = input("Ingrese el nombre del trabajador: ") # Se solicita que ingrese el nombre del trabajador.
    horas_trabajadas = int(input("Ingrese las horas trabajadas: ")) # Se solicita que ingrese las horas trabajadas por el trabajador.
    valor_hora = float(input("Ingrese el valor de la hora: ")) # Se solicita que ingrese el valor de la hora trabajada por el trabajador.
    trabajador = SalarioTrabajador(nombre_trabajador, horas_trabajadas, valor_hora)
    trabajador.mostrar_salario()