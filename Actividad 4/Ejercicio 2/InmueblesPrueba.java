package inmuebles;
import java.util.Scanner;

public class InmueblesPrueba {
    public static void main(String[] args) {
        Scanner EntradaDatos = new Scanner(System.in);
        System.out.println("Ingrese datos Apto Familiar");
        System.out.println("Ingrese Direccion: ");
        String DireccionAptoFamiliar = EntradaDatos.nextLine();
        System.out.println("Ingrese Identificador Inmobiliario: ");
        int IdentificadorInmobiliarioAptoFamiliar = EntradaDatos.nextInt();
        System.out.println("Ingrese Area: ");
        int AreaAptoFamiliar = EntradaDatos.nextInt();
        System.out.println("Ingrese numero de baños: ");
        int NumeroBañosAptoFamiliar = EntradaDatos.nextInt();
        System.out.println("Ingrese Numero habitaciones: ");
        int NumeroHabitacionesAptoFamiliar = EntradaDatos.nextInt();
        System.out.println("Ingrese valor administración: ");
        double PagodeAdministracion = EntradaDatos.nextDouble();
        System.out.println();
        EntradaDatos.nextLine();

        System.out.println("Ingrese datos Apto Familiar");
        System.out.println("Ingrese Direccion: ");
        String DireccionApstudio = EntradaDatos.nextLine();
        System.out.println("Ingrese Identificador Inmobiliario: ");
        int IdentificadorInmobiliarioApstudio = EntradaDatos.nextInt();
        System.out.println("Ingrese Area: ");
        int AreaApstudio = EntradaDatos.nextInt();
        System.out.println("Ingrese numero de baños: ");
        int NumeroBañosApstudio = EntradaDatos.nextInt();
        System.out.println("Ingrese Numero habitaciones: ");
        int NumeroHabitacionesApstudio = EntradaDatos.nextInt();
        System.out.println();
        EntradaDatos.close();

        ApartamentosFamiliares AptoFamil1 = new ApartamentosFamiliares(IdentificadorInmobiliarioAptoFamiliar,AreaAptoFamiliar,DireccionAptoFamiliar, NumeroBañosAptoFamiliar, NumeroHabitacionesAptoFamiliar, PagodeAdministracion);
        Apartaestudios AptoEstu1 = new Apartaestudios(IdentificadorInmobiliarioApstudio, AreaApstudio, DireccionApstudio, NumeroBañosApstudio, NumeroHabitacionesApstudio);
        System.out.println("Datos Apto Familiar:");
        AptoFamil1.CalcularValorVenta(ApartamentosFamiliares.ValorPorMetro);
        AptoFamil1.imprimir();
        System.out.println();

        System.out.println("Datos ApartaEstudio:");
        AptoEstu1.CalcularValorVenta(Apartaestudios.ValorPorMetro);
        AptoEstu1.imprimir();
    }
}