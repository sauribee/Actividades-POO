package inmuebles;

public class Inmuebles {
    protected int IdentificadorInmobiliario;
    protected int AreaM2;
    protected String Direccion;
    protected double PrecioVenta;

    public Inmuebles(int IdentificadorInmobiliario, int AreaM2, String Direccion){
        this.IdentificadorInmobiliario = IdentificadorInmobiliario;
        this.AreaM2 = AreaM2;
        this.Direccion = Direccion;
    }

    public void CalcularValorVenta (double ValorArea){
        PrecioVenta = ValorArea*AreaM2;
    }

    public void imprimir(){
        System.out.println("Identificador Inmobiliario: "+IdentificadorInmobiliario);
        System.out.println("Area (M2): "+AreaM2);
        System.out.println("Dirección: "+Direccion);
        System.out.println("Precio de venta: $"+ PrecioVenta);
    }
}