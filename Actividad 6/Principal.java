import javax.swing.SwingUtilities;

public class Principal {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                GestionContactosGUI ventana = new GestionContactosGUI();
                ventana.setVisible(true);
            }
        });
    }
}