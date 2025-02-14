import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class NotasGUI {

    private JFrame frame;
    private JTextField txtNota1;
    private JTextField txtNota2;
    private JTextField txtNota3;
    private JTextField txtNota4;
    private JTextField txtNota5;
    private JTextArea txtAreaResultado;
    private JScrollPane scrollPane;

    public NotasGUI() {
        frame = new JFrame("Calculadora de Notas");
        frame.setSize(430, 450);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(null);

        JLabel lblNota1 = new JLabel("Nota 1:");
        lblNota1.setBounds(10, 10, 80, 25);
        frame.add(lblNota1);

        txtNota1 = new JTextField();
        txtNota1.setBounds(100, 10, 150, 25);
        frame.add(txtNota1);

        JLabel lblNota2 = new JLabel("Nota 2:");
        lblNota2.setBounds(10, 40, 80, 25);
        frame.add(lblNota2);

        txtNota2 = new JTextField();
        txtNota2.setBounds(100, 40, 150, 25);
        frame.add(txtNota2);

        JLabel lblNota3 = new JLabel("Nota 3:");
        lblNota3.setBounds(10, 70, 80, 25);
        frame.add(lblNota3);

        txtNota3 = new JTextField();
        txtNota3.setBounds(100, 70, 150, 25);
        frame.add(txtNota3);

        JLabel lblNota4 = new JLabel("Nota 4:");
        lblNota4.setBounds(10, 100, 80, 25);
        frame.add(lblNota4);

        txtNota4 = new JTextField();
        txtNota4.setBounds(100, 100, 150, 25);
        frame.add(txtNota4);

        JLabel lblNota5 = new JLabel("Nota 5:");
        lblNota5.setBounds(10, 130, 80, 25);
        frame.add(lblNota5);

        txtNota5 = new JTextField();
        txtNota5.setBounds(100, 130, 150, 25);
        frame.add(txtNota5);

        JButton btnCalcular = new JButton("Calcular");
        btnCalcular.setBounds(40, 160, 120, 25);
        frame.add(btnCalcular);

        JButton btnBorrar = new JButton("Borrar");
        btnBorrar.setBounds(180, 160, 120, 25);
        frame.add(btnBorrar);

        txtAreaResultado = new JTextArea();
        txtAreaResultado.setEditable(false);
        txtAreaResultado.setLineWrap(true);
        txtAreaResultado.setWrapStyleWord(true);

        scrollPane = new JScrollPane(txtAreaResultado);
        scrollPane.setBounds(10, 190, 360, 150);
        frame.add(scrollPane);

        btnCalcular.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                calcularNotas();
            }
        });

        btnBorrar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                borrarCampos();
            }
        });

        frame.setVisible(true);
    }

    private void calcularNotas() {
        try {
            double nota1 = Double.parseDouble(txtNota1.getText());
            double nota2 = Double.parseDouble(txtNota2.getText());
            double nota3 = Double.parseDouble(txtNota3.getText());
            double nota4 = Double.parseDouble(txtNota4.getText());
            double nota5 = Double.parseDouble(txtNota5.getText());

            Notas notas = new Notas();
            notas.listaNotas[0] = nota1;
            notas.listaNotas[1] = nota2;
            notas.listaNotas[2] = nota3;
            notas.listaNotas[3] = nota4;
            notas.listaNotas[4] = nota5;

            double promedio = notas.CalcularPromedio();
            double desviacion = notas.CalcularDesviacionEstandar();
            double menor = notas.CalcularMenorNota();
            double mayor = notas.CalcularMayorNota();

            String resultado = String.format("Promedio: %.2f\nDesviación Estándar: %.2f\nMenor Nota: %.2f\nMayor Nota: %.2f", promedio, desviacion, menor, mayor);
            txtAreaResultado.setText(resultado);

        } catch (NumberFormatException ex) {
            txtAreaResultado.setText("Ingrese datos válidos en todas las notas.");
        }
    }

    private void borrarCampos() {
        txtNota1.setText("");
        txtNota2.setText("");
        txtNota3.setText("");
        txtNota4.setText("");
        txtNota5.setText("");
        txtAreaResultado.setText("");
    }
}