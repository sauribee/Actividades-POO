package cuenta;

public class CuentaCorrientes extends Cuenta {
    private float Sobregiro = 0;

    public CuentaCorrientes(float Saldo, float Tasa_anual){
        super(Saldo, Tasa_anual);
    }

    public void RetirarDinero(float dinero){
        if (dinero>Saldo){
            Sobregiro += (dinero-Saldo);
            Saldo = 0;
        }
        else {
            super.RetirarDinero(dinero);
        }
    }

    public void ConsignarDinero(float dinero){
        if (Sobregiro > 0){
            float residuo = Sobregiro-dinero;
            if (residuo > 0){
                Sobregiro = residuo;
                Saldo = 0;
            }
            else{
                Sobregiro = 0;
                Saldo = -residuo;
            }
        }

        else{
            super.ConsignarDinero(dinero);
        }
    }

    public void CalcularExtractoMensual(){
        super.CalcularExtractoMensual();
    }

    public void imprimir(){
        System.out.println("Saldo: "+Saldo);
        System.out.println("Comisión mensual: "+Comision_mensual);
        System.out.println("Número de transacciones: "+ (Numero_consignaciones+Numero_retiros) );
        System.out.println("Sobregiro: "+Sobregiro);
    }   
}