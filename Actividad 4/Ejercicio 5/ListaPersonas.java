package personas;
import java.util.Vector;

public class ListaPersonas {
    Vector<Persona> listaPersonas;

    public ListaPersonas() {
        listaPersonas = new Vector<>();
    }

    public void eliminarPersona(int i) {
        listaPersonas.removeElementAt(i);
    }

    public void borrarLista() {
        listaPersonas.removeAllElements();
    }
    
    public void añadirPersona(Persona p){
        listaPersonas.add(p);
    }

}