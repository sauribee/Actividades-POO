import tkinter as tk

class Empleado:
    """
    Clase que representa un empleado y permite calcular su salario bruto y neto a partir de las horas trabajadas y el salario por hora.
    """
    def __init__(self, nombre_empleado: str, salario_por_hora: float, horas_trabajadas: int) -> None:
        self.nombre_empleado = nombre_empleado
        self.salario_por_hora = salario_por_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario_empleado(self) -> float:
        return self.salario_por_hora * self.horas_trabajadas

class GUIEmpleado:
    """
    Clase que representa la interfaz gráfica para calcular el salario bruto y neto de un empleado.
    """
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.title("Calculadora de salario")
        self.master.geometry("450x325")
        self.master.resizable(False, False)
        
        self.lbl_nombre = tk.Label(self.master, text="Nombre del empleado:")
        self.lbl_nombre.pack(pady=5)
        self.ent_nombre = tk.Entry(self.master)
        self.ent_nombre.pack(pady=5)

        self.lbl_salario = tk.Label(self.master, text="Salario por hora:")
        self.lbl_salario.pack(pady=5)
        self.ent_salario = tk.Entry(self.master)
        self.ent_salario.pack(pady=5)

        self.lbl_horas = tk.Label(self.master, text="Horas trabajadas:")
        self.lbl_horas.pack(pady=5)
        self.ent_horas = tk.Entry(self.master)
        self.ent_horas.pack(pady=5)

        self.frame_buttons = tk.Frame(self.master)
        self.frame_buttons.pack(pady=10)

        self.btn_calcular_salario = tk.Button(self.frame_buttons, text="Calcular salario", command=self.calcular_salario)
        self.btn_calcular_salario.pack(side=tk.LEFT, padx=5)
        self.btn_limpiar_salario = tk.Button(self.frame_buttons, text="Limpiar salario", command=self.limpiar_salario)
        self.btn_limpiar_salario.pack(side=tk.LEFT, padx=5)

        self.lbl_empleado_salario = tk.Label(self.master, text="")
        self.lbl_empleado_salario.pack(pady=10)
        
    def calcular_salario(self) -> None:
        str_nombre = self.ent_nombre.get()
        flt_salario = float(self.ent_salario.get())
        int_horas = int(self.ent_horas.get())
        empleado = Empleado(str_nombre, flt_salario, int_horas)
        flt_salario_empleado = empleado.calcular_salario_empleado()
        self.lbl_empleado_salario.config(text=f"Nombre del empleado: {str_nombre} \n Salario del empleado: {flt_salario_empleado:.2f}")

    def limpiar_salario(self) -> None:
        self.ent_nombre.delete(0, tk.END)
        self.ent_salario.delete(0, tk.END)
        self.ent_horas.delete(0, tk.END)
        self.lbl_empleado_salario.config(text="")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = GUIEmpleado(root)
    root.mainloop()