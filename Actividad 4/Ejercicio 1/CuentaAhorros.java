package cuenta;

public class CuentaAhorros extends Cuenta{
    private boolean CuentaActiva;

    public CuentaAhorros (float Saldo, float Tasa_anual){
        super(Saldo, Tasa_anual);
        if (Saldo<10000){
            CuentaActiva = false;
        }
        else{
            CuentaActiva = true;
        }
    }

    public void ConsignarDinero(float dinero){
        if (CuentaActiva){
            super.ConsignarDinero(dinero);
        }
    }

    public void RetirarDinero(float dinero){
        if (CuentaActiva){
            super.RetirarDinero(dinero);
        }
    }

    public void CalcularExtractoMensual(){
        if (Numero_retiros > 4){
            Comision_mensual += (Numero_retiros-4)*1000;
            
        }
        super.CalcularExtractoMensual();
        if (Saldo<10000){
            CuentaActiva = false;
        }
    }

    public void imprimir(){
        System.out.println("Saldo: "+Saldo);
        System.out.println("Comisión mensual: "+Comision_mensual);
        System.out.println("Número de transacciones: "+(Numero_consignaciones+Numero_retiros));
    }
}