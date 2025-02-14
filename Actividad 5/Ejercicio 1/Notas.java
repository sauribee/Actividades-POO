public class Notas {
    double[] listaNotas;

    public Notas(){
        listaNotas = new double[5];
    }

    double CalcularPromedio(){
        double SumaNotas = 0;
        for (int i=0;i<listaNotas.length;i++){
            SumaNotas += listaNotas[i];
        }
        double promedio = SumaNotas/listaNotas.length;
        return promedio;
    }

    double CalcularDesviacionEstandar(){
        double promedio = CalcularPromedio();
        double Sumatoria = 0;
        for (int i=0; i<listaNotas.length; i++){
            Sumatoria += Math.pow(listaNotas[i]-promedio, 2);
        }
        double Desviacion = Math.sqrt(Sumatoria/listaNotas.length);
        return Desviacion;
    }

    double CalcularMenorNota(){
        double menor = listaNotas[0];   
        for (int i=0; i<listaNotas.length;i++){
            if (listaNotas[i]<menor){
                menor = listaNotas[i];
            }
        }
        return menor;
    }

    double CalcularMayorNota(){
        double mayor = listaNotas[0];   
        for (int i=0; i<listaNotas.length;i++){
            if (listaNotas[i]>mayor){
                mayor = listaNotas[i];
            }
        }
        return mayor;
    }
}