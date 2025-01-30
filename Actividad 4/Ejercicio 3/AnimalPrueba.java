package animales;

public class AnimalPrueba {
    public static void main(String[] args) {
        Animal[] animales = new Animal[4];
        animales[0] = new Perro();
        animales[1] = new Lobo();
        animales[2] = new Leon();
        animales[3] = new Gato();

        for (int i=0; i<animales.length;i++){
            System.out.println(animales[i].getNombreCientifico());
            System.out.println("Sonído: "+animales[i].getSonido());
            System.out.println("Hábitat: "+animales[i].getHabitat());
            System.out.println("Alimentación: "+animales[i].getAlimentos());
            System.out.println();
        }
    }
}