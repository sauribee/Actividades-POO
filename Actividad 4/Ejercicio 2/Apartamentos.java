package inmuebles;

public class Apartamentos extends InmuebleVivienda {
    public Apartamentos(int IdentificadorInmobiliario, int AreaM2, String Direccion, int NumeroBaños, int NumeroHabitaciones){
        super(IdentificadorInmobiliario, AreaM2, Direccion, NumeroBaños, NumeroHabitaciones);
    }

    public void imprimir(){
        super.imprimir();
    }
}