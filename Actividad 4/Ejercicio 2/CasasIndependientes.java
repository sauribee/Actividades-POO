package inmuebles;

public class CasasIndependientes extends CasasUrbanas {
    protected static double ValorPorMetro = 3000000;
    
    public CasasIndependientes(int IdentificadorInmobiliario, int AreaM2, String Direccion, int NumeroBaños, int NumeroHabitaciones, int NumeroPisos){
        super(IdentificadorInmobiliario, AreaM2, Direccion, NumeroBaños, NumeroHabitaciones, NumeroPisos);
    }
    
    public void imprimir(){
        super.imprimir();
    }
}