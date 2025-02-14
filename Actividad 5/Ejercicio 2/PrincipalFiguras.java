import javax.swing.*;

public class PrincipalFiguras {
    public static void main(String[] args) {
        int opcion;
        String opciones[] = {"Cilindro", "Esfera", "Pirámide"};
        do {
            opcion = JOptionPane.showOptionDialog(null, "Seleccione una figura", "Figuras",
                    JOptionPane.DEFAULT_OPTION, JOptionPane.INFORMATION_MESSAGE, null, opciones, opciones[0]);

            switch (opcion) {
                case 0:
                    VentanaCilindro cilindro = new VentanaCilindro();
                    cilindro.setVisible(true);
                    break;
                case 1:
                    VentanaEsfera esfera = new VentanaEsfera();
                    esfera.setVisible(true);
                    break;
                case 2:
                    VentanaPiramide piramide = new VentanaPiramide();
                    piramide.setVisible(true);
                    break;
                default:
                    break;
            }
        } while (opcion != JOptionPane.CLOSED_OPTION);
    }
}