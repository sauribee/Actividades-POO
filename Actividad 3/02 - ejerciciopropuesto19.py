import math as m
import tkinter as tk

class TrianguloEquilatero:
    """
    Clase que representa un triángulo equilátero y permite calcular su perímetro, altura y área.
    """
    def __init__(self, lado: float) -> None:
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 3 * self.lado

    def calcular_altura(self) -> float:
        return (m.sqrt(3) / 2) * self.lado

    def calcular_area(self) -> float:
        return (m.sqrt(3) / 4) * (self.lado ** 2)

class GUITrianguloEquilatero:
   """
   Clase que representa la interfaz gráfica para el cálculo del perímetro, altura y área de un triángulo equilátero.
   """
   def __init__(self, master: tk.Tk) -> None:
       self.master = master
       self.master.title("Calculadora de triángulo equilátero")
       self.master.geometry("400x175")
       self.master.resizable(False, False)
       
       self.lbl_lado = tk.Label(self.master, text="Lado del triángulo:")
       self.lbl_lado.pack(pady=5)
       self.ent_lado = tk.Entry(self.master)
       self.ent_lado.pack(pady=5)

       self.frame_buttons = tk.Frame(self.master)
       self.frame_buttons.pack(pady=10)

       self.btn_calcular_medidas = tk.Button(self.frame_buttons, text="Calcular medidas", command=self.calcular_medidas)
       self.btn_calcular_medidas.pack(side=tk.LEFT, padx=5)
       self.btn_limpiar_medidas = tk.Button(self.frame_buttons, text="Limpiar medidas", command=self.limpiar_medidas)
       self.btn_limpiar_medidas.pack(side=tk.LEFT, padx=5)

       self.lbl_triangulo_medidas = tk.Label(self.master, text="")
       self.lbl_triangulo_medidas.pack(pady=10)

   def calcular_medidas(self) -> None:
       flt_lado = float(self.ent_lado.get())
       triangulo_equilatero = TrianguloEquilatero(flt_lado)
       flt_perimetro = triangulo_equilatero.calcular_perimetro()
       flt_altura = triangulo_equilatero.calcular_altura()
       flt_area = triangulo_equilatero.calcular_area()
       self.lbl_triangulo_medidas.config(text=f"Perímetro: {flt_perimetro:.2f} \n Altura: {flt_altura:.2f} \n Área: {flt_area:.2f}")

   def limpiar_medidas(self) -> None:
       self.ent_lado.delete(0, tk.END)
       self.lbl_triangulo_medidas.config(text="")
       
if __name__ == "__main__":
    root = tk.Tk()
    app = GUITrianguloEquilatero(root)
    root.mainloop()