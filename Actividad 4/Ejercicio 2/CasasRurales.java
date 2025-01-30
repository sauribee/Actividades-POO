package inmuebles;

public class CasasRurales extends Casas {
    protected static double ValorPorMetro = 1500000;
    protected double DistanciaCabeceraMunicipal;
    protected double AltitudSobreNivelMar;

    public CasasRurales(int IdentificadorInmobiliario, int AreaM2, String Direccion, int NumeroBaños, int NumeroHabitaciones, int NumeroPisos, double DistanciaCabeceraMunicipal, double AltitudSobreNivelMar){
        super(IdentificadorInmobiliario, AreaM2, Direccion, NumeroBaños, NumeroHabitaciones, NumeroPisos);
        this.DistanciaCabeceraMunicipal = DistanciaCabeceraMunicipal;
        this.AltitudSobreNivelMar = AltitudSobreNivelMar;
    }

    public void imprimir(){
        super.imprimir();
        System.out.println("Distancia a la cabecera municipal: " + DistanciaCabeceraMunicipal + " km");
        System.out.println("Altidud sobre nivel del mar: "+ AltitudSobreNivelMar+" metros");
    }
}