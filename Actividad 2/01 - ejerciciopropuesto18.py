class InformacionEmpleado:
    """
    Clase que contiene la información de un empleado y permite calcular su salario bruto y neto en un mes, y mostrar la información del empleado con su salario bruto y neto.
    """
    def __init__(self, codigo_empleado: str, nombres_empleado: str, horas_trabajadas: int, valor_hora: float, retencion_fuente: float) -> None:
        self.codigo_empleado = codigo_empleado
        self.nombres_empleado = nombres_empleado
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.retencion_fuente = retencion_fuente

    def calcular_salario_bruto(self) -> float:   
        return self.horas_trabajadas * self.valor_hora

    def calcular_salario_neto(self) -> float:
        salario_bruto = self.calcular_salario_bruto()
        retencion = salario_bruto * self.retencion_fuente / 100
        return salario_bruto - retencion

    def mostrar_informacion_empleado(self) -> None:
        salario_bruto = self.calcular_salario_bruto()
        salario_neto = self.calcular_salario_neto()
        print(f"Código empleado: {self.codigo_empleado}")
        print(f"Nombres empleado: {self.nombres_empleado}")
        print(f"Salario bruto empleado: {salario_bruto}")
        print(f"Salario neto empleado: {salario_neto}")

if __name__ == "__main__":
    codigo_empleado = input("Ingrese el código del empleado: ") # Se solicita que ingrese el código del empleado.
    nombres_empleado = input("Ingrese los nombres del empleado: ") # Se solicita que ingrese los nombres del empleado.
    horas_trabajadas = int(input("Ingrese las horas trabajadas: ")) # Se solicita que ingrese las horas trabajadas por el empleado.
    valor_hora = float(input("Ingrese el valor de la hora: ")) # Se solicita que ingrese el valor de la hora trabajada por el empleado.
    retencion_fuente = float(input("Ingrese la retención en la fuente: ")) # Se solicita que ingrese el porcentaje de retención en la fuente.
    empleado = InformacionEmpleado(codigo_empleado, nombres_empleado, horas_trabajadas, valor_hora, retencion_fuente)
    empleado.mostrar_informacion_empleado()