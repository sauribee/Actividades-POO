class MatriculaEstudiante:
    """
    Clase que contiene la información de un estudiante y permite calcular el pago por matrícula y mostrar la información del estudiante con el pago por matrícula.
    """
    def __init__(self, numero_inscripcion: str, nombre_estudiante: str, patrimonio: float, estrato_social: int) -> None:
        self.numero_inscripcion = numero_inscripcion
        self.nombres = nombre_estudiante
        self.patrimonio = patrimonio
        self.estrato_social = estrato_social
    
    def calcular_pago_matricula(self) -> float:
        pago_matricula = 50000
        if self.patrimonio > 2000000 and self.estrato_social > 3:
            pago_matricula = pago_matricula + 0.03 * self.patrimonio
        return pago_matricula

    def mostrar_informacion_estudiante(self) -> None:
        pago_matricula = self.calcular_pago_matricula()
        print(f"Número de inscripción del estudiante: {self.numero_inscripcion}")
        print(f"Nombres del estudiante: {self.nombres}")
        print(f"El estudiante debe pagar: ${pago_matricula:.2f}")

if __name__ == "__main__":  
    numero_inscripcion = input("Ingrese el número de inscripción: ") # Se solicita que ingrese el número de inscripción del estudiante.
    nombre_estudiante = input("Ingrese el nombre del estudiante: ") # Se solicita que ingrese el nombre del estudiante.
    patrimonio = float(input("Ingrese el patrimonio del estudiante: ")) # Se solicita que ingrese el patrimonio del estudiante.
    estrato_social = int(input("Ingrese el estrato social del estudiante: ")) # Se solicita que ingrese el estrato social del estudiante.
    estudiante = MatriculaEstudiante(numero_inscripcion, nombre_estudiante, patrimonio, estrato_social)
    estudiante.mostrar_informacion_estudiante()