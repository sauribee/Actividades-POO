package carreraciclistica;
import java.util.Vector;
import java.util.Scanner;

public class Equipo {
    private String nombre;
    private static double totalTiempo;
    private String país;
    private Vector<Ciclista> listaCiclistas;

    public Equipo(String nombre, String país) {
        this.nombre = nombre;
        this.país = país;
        totalTiempo = 0;
        listaCiclistas = new Vector<>();
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    private String getPaís() {
        return país;
    }

    public void setPaís(String país) {
        this.país = país;
    }

    public void añadirCiclista(Ciclista ciclista) {
        listaCiclistas.add(ciclista);
    }

    public void listarEquipo() {
        for (Ciclista c : listaCiclistas) {
            System.out.println(c.getNombre());
        }
    }

    public void buscarCiclista() {
        Scanner sc = new Scanner(System.in);
        String nombreCiclista = sc.next();
        for (Ciclista c : listaCiclistas) {
            if (c.getNombre().equals(nombreCiclista)) {
                System.out.println(c.getNombre());
            }
        }
    }

    public void calcularTotalTiempo() {
        totalTiempo = 0;
        for (Ciclista c : listaCiclistas) {
            totalTiempo += c.getTiempoAcumulado();
        }
    }

    public void imprimir() {
        System.out.println("Nombre del equipo = " + nombre);
        System.out.println("Pais = " + país);
        System.out.println("Total tiempo del equipo = " + totalTiempo);
    }
}