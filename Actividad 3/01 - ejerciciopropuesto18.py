import tkinter as tk

class Empleado:
    """
    Clase que representa un empleado y permite calcular su salario bruto y neto a partir de las horas trabajadas, el valor de la hora y la retención en la fuente.
    """
    def __init__(self, codigo_empleado: str, nombre_empleado: str, horas_trabajadas: int, valor_hora: float, retencion_fuente: float) -> None:
        self.codigo_empleado = codigo_empleado
        self.nombre_empleado = nombre_empleado
        self.horas_trabajadas_mes = horas_trabajadas
        self.valor_hora = valor_hora
        self.retencion_fuente = retencion_fuente

    def calcular_salario_bruto(self) -> float:   
        return self.horas_trabajadas_mes * self.valor_hora

    def calcular_salario_neto(self) -> float:
        salario_bruto = self.calcular_salario_bruto()
        retencion = salario_bruto * ( self.retencion_fuente / 100 )
        return salario_bruto - retencion

class GUIEmpleado:
    """
    Clase que representa la interfaz gráfica para el cálculo del salario bruto y neto de un empleado.
    """
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.title("Calculadora de salario")
        self.master.geometry("450x425")
        self.master.resizable(False, False)
        
        self.lbl_codigo = tk.Label(self.master, text="Código del empleado:")
        self.lbl_codigo.pack(pady=5)
        self.ent_codigo = tk.Entry(self.master)
        self.ent_codigo.pack(pady=5)

        self.lbl_nombre = tk.Label(self.master, text="Nombre del empleado:")
        self.lbl_nombre.pack(pady=5)
        self.ent_nombre = tk.Entry(self.master)
        self.ent_nombre.pack(pady=5)

        self.lbl_horas = tk.Label(self.master, text="Horas trabajadas en el mes:")
        self.lbl_horas.pack(pady=5)
        self.ent_horas = tk.Entry(self.master)
        self.ent_horas.pack(pady=5)

        self.lbl_valor = tk.Label(self.master, text="Valor de la hora:")
        self.lbl_valor.pack(pady=5)
        self.ent_valor = tk.Entry(self.master)
        self.ent_valor.pack(pady=5)
        
        self.lbl_retencion = tk.Label(self.master, text="Retención en la fuente:")
        self.lbl_retencion.pack(pady=5)
        self.ent_retencion = tk.Entry(self.master)
        self.ent_retencion.pack(pady=5)

        self.frame_buttons = tk.Frame(self.master)
        self.frame_buttons.pack(pady=10)

        self.btn_calcular_salario = tk.Button(self.frame_buttons, text="Calcular salario", command=self.calcular_salario)
        self.btn_calcular_salario.pack(side=tk.LEFT, padx=5)
        self.btn_limpiar_salario = tk.Button(self.frame_buttons, text="Limpiar salario", command=self.limpiar_salario)
        self.btn_limpiar_salario.pack(side=tk.RIGHT, padx=5)

        self.lbl_empleado_informacion = tk.Label(self.master, text="")
        self.lbl_empleado_informacion.pack(pady=10)

    def calcular_salario(self) -> None:
        str_codigo = self.ent_codigo.get()
        str_nombre = self.ent_nombre.get()
        int_horas = int(self.ent_horas.get())
        flt_valor = float(self.ent_valor.get())
        flt_retencion = float(self.ent_retencion.get())
        empleado = Empleado(str_codigo, str_nombre, int_horas, flt_valor, flt_retencion)
        flt_salario_bruto = empleado.calcular_salario_bruto()
        flt_salario_neto = empleado.calcular_salario_neto()
        str_empleado_informacion = f"Código del empleado: {str_codigo} \n Nombre del empleado: {str_nombre} \n Salario bruto: {flt_salario_bruto:.2f} \n Salario neto: {flt_salario_neto:.2f}"
        self.lbl_empleado_informacion.config(text=str_empleado_informacion)

    def limpiar_salario(self) -> None:
        self.ent_codigo.delete(0, tk.END)
        self.ent_nombre.delete(0, tk.END)
        self.ent_horas.delete(0, tk.END)
        self.ent_valor.delete(0, tk.END)
        self.ent_retencion.delete(0, tk.END)
        self.lbl_empleado_informacion.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUIEmpleado(root)
    root.mainloop()