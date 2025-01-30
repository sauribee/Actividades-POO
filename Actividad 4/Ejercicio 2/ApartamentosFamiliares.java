package inmuebles;

public class ApartamentosFamiliares extends Apartamentos {
    protected double PagoAdministracion;
    protected static double ValorPorMetro = 2000000;

    public ApartamentosFamiliares(int IdentificadorInmobiliario, int AreaM2, String Direccion, int NumeroBaños, int NumeroHabitaciones, double PagoAdministracion){
        super(IdentificadorInmobiliario, AreaM2, Direccion, NumeroBaños, NumeroHabitaciones);
        this.PagoAdministracion = PagoAdministracion;
    }

    public void imprimir(){
        super.imprimir();
        System.out.println("Valor de la administración: $"+PagoAdministracion);
    }
}