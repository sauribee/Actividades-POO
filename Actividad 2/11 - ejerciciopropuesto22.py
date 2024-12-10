class InformacionEmpleado:
    """
    Clase que contiene la información de un empleado y permite calcular su salario bruto y neto en un mes, y mostrar la información del empleado con su salario bruto y neto.
    """
    def __init__(self, nombre_empleado: str, salario_por_hora: float, horas_trabajadas: int) -> None:
        self.nombre_empleado = nombre_empleado
        self.salario_por_hora = salario_por_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario_empleado(self) -> float:
        return self.salario_por_hora * self.horas_trabajadas

    def mostrar_informacion_empleado(self) -> None:
        salario_mensual = self.calcular_salario_empleado()
        if salario_mensual > 450000:
            print(f"Nombre del empleado: {self.nombre_empleado}")
            print(f"Salario del empleado: ${salario_mensual:.2f}")
        else:
            print(f"Nombre del empleado: {self.nombre_empleado}")

if __name__ == "__main__":
    nombre_empleado = input("Ingrese el nombre del empleado: ") # Se solicita que ingrese el nombre del empleado.
    salario_por_hora = float(input("Ingrese el salario por hora: ")) # Se solicita que ingrese el salario por hora del empleado.
    horas_trabajadas = int(input("Ingrese las horas trabajadas en el mes: ")) # Se solicita que ingrese las horas trabajadas en el mes por el empleado.
    empleado = InformacionEmpleado(nombre_empleado, salario_por_hora, horas_trabajadas)
    empleado.mostrar_informacion_empleado()