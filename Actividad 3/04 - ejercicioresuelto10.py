import tkinter as tk

class Estudiante:
    """
    Clase que representa un estudiante y permite calcular el pago por matrícula a partir de su patrimonio y estrato social.
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

class GUIEstudiante:
    """
    Clase que representa la interfaz gráfica para calcular el pago por matrícula de un estudiante.
    """
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.title("Calculadora de matrícula")
        self.master.geometry("400x400")
        self.master.resizable(False, False)
        
        self.lbl_numero_inscripcion = tk.Label(self.master, text="Número de inscripción:")
        self.lbl_numero_inscripcion.pack(pady=5)
        self.ent_numero_inscripcion = tk.Entry(self.master)
        self.ent_numero_inscripcion.pack(pady=5)

        self.lbl_nombre_estudiante = tk.Label(self.master, text="Nombre del estudiante:")
        self.lbl_nombre_estudiante.pack(pady=5)
        self.ent_nombre_estudiante = tk.Entry(self.master)
        self.ent_nombre_estudiante.pack(pady=5)

        self.lbl_patrimonio = tk.Label(self.master, text="Patrimonio:")
        self.lbl_patrimonio.pack(pady=5)
        self.ent_patrimonio = tk.Entry(self.master)
        self.ent_patrimonio.pack(pady=5)

        self.lbl_estrato = tk.Label(self.master, text="Estrato social:")
        self.lbl_estrato.pack(pady=5)
        self.ent_estrato = tk.Entry(self.master)
        self.ent_estrato.pack(pady=5)

        self.frame_buttons = tk.Frame(self.master)
        self.frame_buttons.pack(pady=10)

        self.btn_calcular_matricula = tk.Button(self.frame_buttons, text="Calcular matrícula", command=self.calcular_matricula)
        self.btn_calcular_matricula.pack(side=tk.LEFT, padx=5)
        self.btn_limpiar_matricula = tk.Button(self.frame_buttons, text="Limpiar matrícula", command=self.limpiar_matricula)
        self.btn_limpiar_matricula.pack(side=tk.LEFT, padx=5)

        self.lbl_resultado = tk.Label(self.master, text="")
        self.lbl_resultado.pack(pady=10)
        
    def calcular_matricula(self) -> None:
        str_numero_inscripcion = self.ent_numero_inscripcion.get()
        str_nombre_estudiante = self.ent_nombre_estudiante.get()
        flt_patrimonio = float(self.ent_patrimonio.get())
        int_estrato_social = int(self.ent_estrato.get())
        estudiante = Estudiante(str_numero_inscripcion, str_nombre_estudiante, flt_patrimonio, int_estrato_social)
        flt_pago_matricula = estudiante.calcular_pago_matricula()
        self.lbl_resultado.config(text=f"Número de inscripción: {str_numero_inscripcion} \n Nombre del estudiante: {str_nombre_estudiante} \n Pago por matrícula: {flt_pago_matricula:.2f}")
        
    def limpiar_matricula(self) -> None:
        self.ent_numero_inscripcion.delete(0, tk.END)
        self.ent_nombre_estudiante.delete(0, tk.END)
        self.ent_patrimonio.delete(0, tk.END)
        self.ent_estrato.delete(0, tk.END)
        self.lbl_resultado.config(text="")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = GUIEstudiante(root)
    root.mainloop()