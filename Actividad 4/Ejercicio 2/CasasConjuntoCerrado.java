package inmuebles;

public class CasasConjuntoCerrado extends CasasUrbanas {
    protected static double ValorPorMetro = 2500000;
    protected double ValorAdministracion;
    protected boolean IncluyePiscina;
    protected boolean IncluyeCampoDeportivo;

    public CasasConjuntoCerrado(int IdentificadorInmobiliario, int AreaM2, String Direccion, int NumeroBaños, int NumeroHabitaciones, int NumeroPisos, double ValorAdministracion, boolean IncluyePiscina, boolean IncluyeCampoDeportivo){
        super(IdentificadorInmobiliario, AreaM2, Direccion, NumeroBaños, NumeroHabitaciones, NumeroPisos);
        this.ValorAdministracion = ValorAdministracion;
        this.IncluyeCampoDeportivo = IncluyeCampoDeportivo;
        this.IncluyePiscina = IncluyePiscina;
    }

    public void imprimir(){
        super.imprimir();
        System.out.println("Valor Administración: "+ ValorAdministracion);
        System.out.println("Tiene Campos Deportivos?: "+IncluyeCampoDeportivo);
        System.out.println("Tiene piscina?: " + IncluyePiscina);
    }
}