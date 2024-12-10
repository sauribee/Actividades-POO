class PromocionAlmacen:
    """
    Clase que permite calcular el valor final de una compra a partir de un valor de compra y el color de una bolita, y mostrar el valor final de la compra.
    """
    def __init__(self, valor_compra: float, color_bolita: str) -> None:
        self.valor_compra = valor_compra
        self.color_bolita = color_bolita.lower()

    def calcular_valor_final(self) -> float:
        if self.color_bolita == "blanca":
            descuento = 0
        elif self.color_bolita == "verde":
            descuento = 10
        elif self.color_bolita == "amarilla":
            descuento = 25
        elif self.color_bolita == "azul":
            descuento = 50
        else:  
            descuento = 100
        valor_final = self.valor_compra - (self.valor_compra * descuento / 100)
        return valor_final

    def mostrar_valor_final(self) -> None:
        valor_final = self.calcular_valor_final()
        print(f"El cliente debe pagar: ${valor_final:.2f}")

if __name__ == "__main__":
    valor_compra = float(input("Ingrese el valor de la compra: ")) # Se solicita que ingrese el valor de la compra.
    color_bolita = input("Ingrese el color de la bolita: ") # Se solicita que ingrese el color de la bolita.
    promocion = PromocionAlmacen(valor_compra, color_bolita)
    promocion.mostrar_valor_final()