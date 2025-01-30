package inmuebles;

public class InmuebleVivienda extends Inmuebles {
    protected int NumeroBaños;
    protected int NumeroHabitaciones;

    public InmuebleVivienda(int IdentificadorInmobiliario, int AreaM2, String Direccion, int NumeroBaños, int NumeroHabitaciones){
        super(IdentificadorInmobiliario, AreaM2, Direccion);
        this.NumeroBaños = NumeroBaños;
        this.NumeroHabitaciones = NumeroHabitaciones;
    }

    public void imprimir(){
        super.imprimir();
        System.out.println("Número de habitaciones: "+NumeroHabitaciones);
        System.out.println("Número de baños: "+NumeroBaños);
    }
}