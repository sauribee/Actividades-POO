package inmuebles;

public class Apartaestudios extends Apartamentos {
    protected static double ValorPorMetro = 1500000;

    public Apartaestudios(int IdentificadorInmobiliario, int AreaM2, String Direccion, int NumeroBaños, int NumeroHabitaciones){
        super(IdentificadorInmobiliario, AreaM2, Direccion, 1,1);
    }

    public void imprimir(){
        super.imprimir();
    }
}