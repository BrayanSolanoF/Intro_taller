
 import java.util.Scanner;
public class Figure {

    public static void main(String Args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese valores del triangulo");
        int valor= sc.nextInt();
        triangle(valor);

    }

    public static void triangle(int valor){
        String t="";

        for (int i=0; i<valor;i++){
            t+="*";



            System.out.println(t);
        }



    }
}