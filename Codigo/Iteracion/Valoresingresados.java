import java.util.Scanner;

public class Valoresingresados {

    public static void main(String Args[]) {


        int suma2 = suma();
        System.out.println("Suma "+ suma2);


    }

    public static int suma() {
        int suma1 = 0;
        boolean valor = true;
        Scanner sc = new Scanner(System.in);
        int num = 0;

        while (valor == true) {
            System.out.println("Ingrese valores, 0 para detener");
            num = sc.nextInt();
            suma1 += num;
            if (num == 0) {

                valor = false;
            }




        }
        return suma1;


    }
}