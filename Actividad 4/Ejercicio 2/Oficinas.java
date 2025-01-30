package inmuebles;

public class Oficinas extends Locales {
    protected boolean EsGubernamental;
    protected static double ValorPorMetro = 3500000;

    public Oficinas (int IdentificadorInmobiliario, int AreaM2, String Direccion, boolean EsGubernamental, tipo TipoLocal){
        super(IdentificadorInmobiliario, AreaM2, Direccion, TipoLocal);
        this.EsGubernamental = EsGubernamental;
    }

    public void imprimir(){
        super.imprimir();
        System.out.println("La oficina es gubernamental?: "+EsGubernamental);
    }
}