package inmuebles;

public class CasasUrbanas extends Casas { 
    
    public CasasUrbanas(int IdentificadorInmobiliario, int AreaM2, String Direccion, int NumeroBaños, int NumeroHabitaciones, int NumeroPisos){
        super(IdentificadorInmobiliario, AreaM2, Direccion, NumeroBaños, NumeroHabitaciones, NumeroPisos);
    }

    public void imprimir(){
        super.imprimir();
    }

}