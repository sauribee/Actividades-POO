package carreraciclistica;

public class EquipoPrueba {
    public static void main(String[] args) {
        Equipo equipo1 = new Equipo("INEOS", "Reino Unido");
        Velocista velocista1 = new Velocista(123, "Samuel", 220, 28);
        Escalador escalador1 = new Escalador(1234, "Primo Roglic", 24, 15);
        Contrarrelojista contrarrelojista1 = new Contrarrelojista(12345, "Jonas Vingegaard", 100);

        equipo1.añadirCiclista(velocista1);
        equipo1.añadirCiclista(escalador1);
        equipo1.añadirCiclista(contrarrelojista1);

        velocista1.setTiempoAcumulado(375);
        escalador1.setTiempoAcumulado(390);
        contrarrelojista1.setTiempoAcumulado(360);

        equipo1.calcularTotalTiempo();
        equipo1.imprimir();
        equipo1.listarEquipo();
    }
}