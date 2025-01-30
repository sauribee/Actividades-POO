package inmuebles;

public class LocalesComerciales extends Locales {
    protected static double ValorPorMetro = 3000000;
    protected String NombreCentroComercial;

    public LocalesComerciales(int IdentificadorInmobiliario, int AreaM2, String Direccion, String NombreCentroComercial, tipo TipoLocal){
        super(IdentificadorInmobiliario, AreaM2, Direccion, TipoLocal);
        this.NombreCentroComercial = NombreCentroComercial;
    }

    public void imprimir(){
        super.imprimir();
        System.out.println("Centro Comercial: "+NombreCentroComercial);
    }
}