package animales;

public abstract class Animal{
    protected String sonido;
    protected String Alimentos;
    protected String Habitat;
    protected String NombreCientifico;

    public abstract String getSonido();
    public abstract String getAlimentos();
    public abstract String getHabitat();
    public abstract String getNombreCientifico();
}