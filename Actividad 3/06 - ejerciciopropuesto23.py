import math as m
import tkinter as tk

class EcuacionSegundoGrado:
    """
    Clase que representa una ecuación de segundo grado ax^2+bx+c=0 y permite calcular sus soluciones reales.
    """
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

    def calcular_discriminante_ecuacion(self) -> float:
        return self.b ** 2 - 4 * self.a * self.c

    def calcular_soluciones_ecuacion(self) -> tuple:
        discriminante = self.calcular_discriminante_ecuacion()
        if discriminante < 0:
            return None, None
        else:
            x1 = (-self.b + m.sqrt(discriminante)) / (2 * self.a)
            x2 = (-self.b - m.sqrt(discriminante)) / (2 * self.a)
            return x1, x2

class GUIEcuacionSegundoGrado:
    """
    Clase que representa la interfaz gráfica para el cálculo de las soluciones reales de una ecuación de segundo grado.
    """
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.title("Soluciones de ecuación de segundo grado")
        self.master.geometry("400x350")
        self.master.resizable(False, False)
        
        self.lbl_a = tk.Label(self.master, text="Coeficiente a:")
        self.lbl_a.pack(pady=5)
        self.ent_a = tk.Entry(self.master)
        self.ent_a.pack(pady=5)

        self.lbl_b = tk.Label(self.master, text="Coeficiente b:")
        self.lbl_b.pack(pady=5)
        self.ent_b = tk.Entry(self.master)
        self.ent_b.pack(pady=5)

        self.lbl_c = tk.Label(self.master, text="Coeficiente c:")
        self.lbl_c.pack(pady=5)
        self.ent_c = tk.Entry(self.master)
        self.ent_c.pack(pady=5)
        
        self.frame_buttons = tk.Frame(self.master)
        self.frame_buttons.pack(pady=10)

        self.btn_calcular_soluciones = tk.Button(self.frame_buttons, text="Calcular soluciones", command=self.calcular_soluciones)
        self.btn_calcular_soluciones.pack(side=tk.LEFT, padx=5)
        self.btn_limpiar_soluciones = tk.Button(self.frame_buttons, text="Limpiar soluciones", command=self.limpiar_soluciones)
        self.btn_limpiar_soluciones.pack(side=tk.LEFT, padx=5)

        self.lbl_ecuacion_soluciones = tk.Label(self.master, text="")
        self.lbl_ecuacion_soluciones.pack(pady=10)

    def calcular_soluciones(self) -> None:
        flt_a = float(self.ent_a.get())
        flt_b = float(self.ent_b.get())
        flt_c = float(self.ent_c.get())
        ecuacion_segundo_grado = EcuacionSegundoGrado(flt_a, flt_b, flt_c)
        flt_x1, flt_x2 = ecuacion_segundo_grado.calcular_soluciones_ecuacion()
        if flt_x1 is None:
            self.lbl_ecuacion_soluciones.config(text="La ecuación no tiene soluciones reales")
        else:
            self.lbl_ecuacion_soluciones.config(text=f"Solución 1: {flt_x1:.2f} \n Solución 2: {flt_x2:.2f}")
            
    def limpiar_soluciones(self) -> None:
        self.ent_a.delete(0, tk.END)
        self.ent_b.delete(0, tk.END)
        self.ent_c.delete(0, tk.END)
        self.lbl_ecuacion_soluciones.config(text="")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = GUIEcuacionSegundoGrado(root)
    root.mainloop()