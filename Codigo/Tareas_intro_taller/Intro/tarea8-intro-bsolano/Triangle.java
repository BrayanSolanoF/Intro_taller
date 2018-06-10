import javax.swing.JOptionPane;
import java.util.Scanner;

public class Triangle
{
  public static void main(String args[])
  {
    
    int num;
    num=Integer.parseInt(JOptionPane.showInputDialog("Digite la altura del tri�ngulo"));
    String triangle=triangle(num);
    JOptionPane.showMessageDialog(null,"Altura: "+num+"\n"+triangle);
  }
  
  public static String triangle(int num)
  {
    String triangulo="";
    String resultado="";
    for (int contador=0;contador<num;contador++)
    {
      triangulo+="*";
      resultado+=triangulo+"\n";
    }
    return resultado;
    
  }
}