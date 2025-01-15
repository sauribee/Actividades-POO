import math as m
import tkinter as tk

class Circulo:
    """
    Clase que representa un círculo y permite calcular su área y perímetro.
    """
    def __init__(self, radio: float) -> None:
        self.radio = radio

    def calcular_area(self) -> float:
        return m.pi * (self.radio ** 2)

    def calcular_perimetro(self) -> float:
        return 2 * m.pi * self.radio

class Rectangulo:
    """
    Clase que representa un rectángulo y permite calcular su área y perímetro.
    """
    def __init__(self, base: float, altura: float) -> None:    
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        return 2 * (self.base + self.altura)

class Cuadrado:
    """
    Clase que representa un cuadrado y permite calcular su área y perímetro.
    """
    def __init__(self, lado: float) -> None:
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado ** 2

    def calcular_perimetro(self) -> float:
        return 4 * self.lado

class TrianguloRectangulo:
    """
    Clase que representa un triángulo rectángulo y permite calcular su área, perímetro y determinar el tipo de triángulo que es.
    """
    def __init__(self, base: float, altura: float) -> None:
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2

    def calcular_perimetro(self) -> float:
        return self.base + self.altura + self.calcular_hipotenusa()

    def calcular_hipotenusa(self) -> float:
        return m.sqrt(self.base ** 2 + self.altura ** 2)

    def tipo_triangulo(self) -> str:
        hipotenusa = self.calcular_hipotenusa()
        if self.base == self.altura == hipotenusa:
            return "Equilátero"
        elif self.base == self.altura or self.base == hipotenusa or self.altura == hipotenusa:
            return "Isósceles"
        else:
            return "Escaleno"

class GUIFigurasGeometricas:
    """
    Clase que representa la interfaz gráfica para el cálculo de las áreas y perímetros de figuras geométricas.
    """
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.title("Calculadora de figuras geométricas")
        self.master.geometry("500x400")
        self.master.resizable(False, False)
        
        self.lbl_figura = tk.Label(self.master, text="Seleccione la figura:")
        self.lbl_figura.pack(pady=5)
        self.var_figura = tk.StringVar()
        self.var_figura.set("Círculo")
        self.opt_figura = tk.OptionMenu(self.master, self.var_figura, "Círculo", "Rectángulo", "Cuadrado", "Triángulo rectángulo", command=self.mostrar_parametros)
        self.opt_figura.pack(pady=5)
        
        self.frame_parametros = tk.Frame(self.master)
        self.frame_parametros.pack(pady=10)
        
        self.lbl_radio = tk.Label(self.frame_parametros, text="Radio del círculo:")
        self.ent_radio = tk.Entry(self.frame_parametros)
        
        self.lbl_base = tk.Label(self.frame_parametros, text="Base del rectángulo:")
        self.ent_base = tk.Entry(self.frame_parametros)
        
        self.lbl_altura = tk.Label(self.frame_parametros, text="Altura del rectángulo:")
        self.ent_altura = tk.Entry(self.frame_parametros)
        
        self.lbl_lado = tk.Label(self.frame_parametros, text="Lado del cuadrado:")
        self.ent_lado = tk.Entry(self.frame_parametros)
        
        self.lbl_base_triangulo = tk.Label(self.frame_parametros, text="Base del triángulo:")
        self.ent_base_triangulo = tk.Entry(self.frame_parametros)
        
        self.lbl_altura_triangulo = tk.Label(self.frame_parametros, text="Altura del triángulo:")
        self.ent_altura_triangulo = tk.Entry(self.frame_parametros)
        
        self.frame_buttons = tk.Frame(self.master)
        self.frame_buttons.pack(pady=10)
        
        self.btn_calcular_medidas = tk.Button(self.frame_buttons, text="Calcular medidas", command=self.calcular_medidas)
        self.btn_calcular_medidas.pack(side=tk.LEFT, padx=5)
        self.btn_limpiar_medidas = tk.Button(self.frame_buttons, text="Limpiar medidas", command=self.limpiar_medidas)
        self.btn_limpiar_medidas.pack(side=tk.LEFT, padx=5)
        
        self.lbl_figura_medidas = tk.Label(self.master, text="")
        self.lbl_figura_medidas.pack(pady=10)
        
        self.mostrar_parametros("Círculo")
        
    def mostrar_parametros(self, figura: str) -> None:
        for widget in self.frame_parametros.winfo_children():
            widget.pack_forget()
        
        if figura == "Círculo":
            self.lbl_radio.pack(pady=5)
            self.ent_radio.pack(pady=5)
        elif figura == "Rectángulo":
            self.lbl_base.pack(pady=5)
            self.ent_base.pack(pady=5)
            self.lbl_altura.pack(pady=5)
            self.ent_altura.pack(pady=5)
        elif figura == "Cuadrado":
            self.lbl_lado.pack(pady=5)
            self.ent_lado.pack(pady=5)
        elif figura == "Triángulo rectángulo":
            self.lbl_base_triangulo.pack(pady=5)
            self.ent_base_triangulo.pack(pady=5)
            self.lbl_altura_triangulo.pack(pady=5)
            self.ent_altura_triangulo.pack(pady=5)
        
    def calcular_medidas(self) -> None:
        figura = self.var_figura.get()
        if figura == "Círculo":
            flt_radio = float(self.ent_radio.get())
            circulo = Circulo(flt_radio)
            flt_area = circulo.calcular_area()
            flt_perimetro = circulo.calcular_perimetro()
            self.lbl_figura_medidas.config(text=f"Área: {flt_area:.2f} \n Perímetro: {flt_perimetro:.2f}")
        elif figura == "Rectángulo":
            flt_base = float(self.ent_base.get())
            flt_altura = float(self.ent_altura.get())
            rectangulo = Rectangulo(flt_base, flt_altura)
            flt_area = rectangulo.calcular_area()
            flt_perimetro = rectangulo.calcular_perimetro()
            self.lbl_figura_medidas.config(text=f"Área: {flt_area:.2f} \n Perímetro: {flt_perimetro:.2f}")
        elif figura == "Cuadrado":
            flt_lado = float(self.ent_lado.get())
            cuadrado = Cuadrado(flt_lado)
            flt_area = cuadrado.calcular_area()
            flt_perimetro = cuadrado.calcular_perimetro()
            self.lbl_figura_medidas.config(text=f"Área: {flt_area:.2f} \n Perímetro: {flt_perimetro:.2f}")
        elif figura == "Triángulo rectángulo":
            flt_base = float(self.ent_base_triangulo.get())
            flt_altura = float(self.ent_altura_triangulo.get())
            triangulo_rectangulo = TrianguloRectangulo(flt_base, flt_altura)
            flt_area = triangulo_rectangulo.calcular_area()
            flt_perimetro = triangulo_rectangulo.calcular_perimetro()
            flt_hipotenusa = triangulo_rectangulo.calcular_hipotenusa()
            str_tipo_triangulo = triangulo_rectangulo.tipo_triangulo()
            self.lbl_figura_medidas.config(text=f"Área: {flt_area:.2f} \n Perímetro: {flt_perimetro:.2f} \n Hipotenusa: {flt_hipotenusa:.2f} \n Tipo de triángulo: {str_tipo_triangulo}")
            
    def limpiar_medidas(self) -> None:
        self.ent_radio.delete(0, tk.END)
        self.ent_base.delete(0, tk.END)
        self.ent_altura.delete(0, tk.END)
        self.ent_lado.delete(0, tk.END)
        self.ent_base_triangulo.delete(0, tk.END)
        self.ent_altura_triangulo.delete(0, tk.END)
        self.lbl_figura_medidas.config(text="")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = GUIFigurasGeometricas(root)
    root.mainloop()