import tkinter as tk 

class ComparadorNumerosEnteros:
    """
    Clase que permite comparar dos números enteros y determinar cuál es mayor, menor o si son iguales.
    """    
    def __init__(self, numero_A: int, numero_B: int) -> None:
        self.numero_A = numero_A
        self.numero_B = numero_B

    def comparar_numeros_enteros(self) -> str:
        if self.numero_A > self.numero_B:
            return f"{self.numero_A} es mayor que {self.numero_B}"
        elif self.numero_A == self.numero_B:
            return f"{self.numero_A} es igual a {self.numero_B}"
        else:
            return f"{self.numero_A} es menor que {self.numero_B}"
        
class GUIComparadorNumerosEnteros:
    """
    Clase que representa la interfaz gráfica para comparar dos números.
    """
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.title("Comparador de números")
        self.master.geometry("350x200")
        self.master.resizable(False, False)
        
        self.lbl_numero_A = tk.Label(self.master, text="Número A:")
        self.lbl_numero_A.pack(pady=5)
        self.ent_numero_A = tk.Entry(self.master)
        self.ent_numero_A.pack(pady=5)

        self.lbl_numero_B = tk.Label(self.master, text="Número B:")
        self.lbl_numero_B.pack(pady=5)
        self.ent_numero_B = tk.Entry(self.master)
        self.ent_numero_B.pack(pady=5)

        self.frame_buttons = tk.Frame(self.master)
        self.frame_buttons.pack(pady=10)

        self.btn_comparar_numeros = tk.Button(self.frame_buttons, text="Comparar números", command=self.comparar_numeros)
        self.btn_comparar_numeros.pack(side=tk.LEFT, padx=5)
        self.btn_limpiar_numeros = tk.Button(self.frame_buttons, text="Limpiar números", command=self.limpiar_numeros)
        self.btn_limpiar_numeros.pack(side=tk.LEFT, padx=5)

        self.lbl_comparacion_numeros = tk.Label(self.master, text="")
        self.lbl_comparacion_numeros.pack(pady=10)
        
    def comparar_numeros(self) -> None:
        int_numero_A = int(self.ent_numero_A.get())
        int_numero_B = int(self.ent_numero_B.get())
        comparador = ComparadorNumerosEnteros(int_numero_A, int_numero_B)
        str_comparacion_numeros = comparador.comparar_numeros_enteros()
        self.lbl_comparacion_numeros.config(text=str_comparacion_numeros)
        
    def limpiar_numeros(self) -> None:
        self.ent_numero_A.delete(0, tk.END)
        self.ent_numero_B.delete(0, tk.END)
        self.lbl_comparacion_numeros.config(text="")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = GUIComparadorNumerosEnteros(root)
    root.mainloop()