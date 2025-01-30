package cuenta;

import java.util.Scanner;
public class CuentaPrueba {
    
    public static void main(String[] args) {
        Scanner EntradaDatos = new Scanner(System.in);
        System.out.print("Ingrese saldo inicial: $");
        float SaldoInicial = EntradaDatos.nextFloat();
        System.out.print("Ingrese Tasa Interes anual: $");
        float TasaInteres = EntradaDatos.nextFloat();
        CuentaAhorros CuentaAhorros1 = new CuentaAhorros(SaldoInicial,TasaInteres);
        System.out.print("Ingrese cantidad a consignar: $");
        float CantidadConsignar = EntradaDatos.nextFloat();
        CuentaAhorros1.ConsignarDinero(CantidadConsignar);
        System.out.print("Ingrese cantidad a retirar: $");
        float CantidadRetirar = EntradaDatos.nextFloat();
        CuentaAhorros1.RetirarDinero(CantidadRetirar);
        CuentaAhorros1.CalcularExtractoMensual();
        CuentaAhorros1.imprimir();
        EntradaDatos.close();
    }
}