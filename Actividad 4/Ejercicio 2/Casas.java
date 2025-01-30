package inmuebles;

public class Casas extends InmuebleVivienda {
    protected int NumeroPisos;

    public Casas(int IdentificadorInmobiliario, int AreaM2, String Direccion, int NumeroBaños, int NumeroHabitaciones, int NumeroPisos){
        super(IdentificadorInmobiliario, AreaM2, Direccion, NumeroBaños, NumeroHabitaciones);
        this.NumeroPisos = NumeroPisos;
    }

    public void imprimir(){
        super.imprimir();
        System.out.println("Número de pisos: "+NumeroPisos);
    }
}