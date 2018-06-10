import java.util.Scanner;

public class Busquedabinario {
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int lista[]=llenarArray();
        System.out.println("Ingrese valor a buscar");
        int valor = sc.nextInt();
        boolean encontrado = buscar(lista,valor);
        if(encontrado == true){
            System.out.println("EL valor se encuentra en la lista");
        }
        else{
            System.out.println("EL valor no se encuentra en la lista");
        }


    }

    public static int[] llenarArray()
    {
        int lista[];
        int longitud;
        int valor=0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese longitud");
        longitud = sc.nextInt();
        lista=new int[longitud];
        for (int contador=0;contador<longitud;contador++)
        {
            System.out.println("Ingrese valor");
            valor= sc.nextInt();
            lista[contador]=valor;
        }
        return lista;
    }

    public static boolean buscar(int[] lista, int valor)
    {
        int topeList = lista.length-1;
        int pos;
        boolean encontrado = false;

        for(int inicioList=0; inicioList <= topeList; )
        {
            pos = (inicioList+topeList)/2;
            if (valor == lista[pos])
            {
                encontrado = true;
                return encontrado;
            }
            else if (lista[pos] < valor)
            {
                inicioList = pos+1;
            }
            else if (lista[pos] > valor )
            {
                topeList = pos-1;
            }
        }
        return encontrado;
    }
}