package cuenta;

public class Cuenta {
    protected float Saldo;
    protected int Numero_consignaciones = 0;
    protected int Numero_retiros = 0;
    protected float Tasa_anual;
    protected float Comision_mensual = 0;

    public Cuenta(float Saldo, float Tasa_anual){
        this.Saldo = Saldo;
        this.Tasa_anual = Tasa_anual;
    }

    public void ConsignarDinero(float dinero){
        if(dinero<=Saldo && dinero>0){
        Saldo += dinero;
        Numero_consignaciones += 1;
        }
    }

    public void RetirarDinero (float dinero){
        if (dinero<=Saldo && dinero>0){
            Saldo -= dinero;
            Numero_retiros += 1;
        }
        else{
            System.err.println("El valor a retirar excede la cantidad de dinero en la cuenta");
        }
    }

    public void CalcularInteresMensual(){
        float Tasa_Mensual = (Tasa_anual/12);
        Saldo += Saldo*Tasa_Mensual;
    }

    public void CalcularExtractoMensual(){
        Saldo -= Comision_mensual;
        CalcularInteresMensual();
    }

    public void imprimir(){
        System.out.println("Saldo: "+Saldo);
        System.out.println("Número de consignaciones: "+Numero_consignaciones);
        System.out.println("Número de retiros: "+Numero_retiros);
        System.out.println("Tasa anual: "+Tasa_anual+"%");
        System.out.println("Comisión mensual: "+Comision_mensual);
    }
}