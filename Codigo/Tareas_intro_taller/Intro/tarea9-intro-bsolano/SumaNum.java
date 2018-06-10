import javax.swing.JOptionPane;

public class SumaNum {
    
     public static void main(String args[])
  {
    int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un n�mero distinto de cero para iniciar con la suma"));
    
    if(numero != 0){
        int suma = sumar(numero);
        JOptionPane.showMessageDialog(null,"El resultado de la suma es: "+ suma);
    }
    else{
        JOptionPane.showMessageDialog(null,"El n�mero digitado tiene que ser distinto de cero");
    }
    

  }
  
  public static int sumar(int numero)
  {
    int suma = numero;
    
    while(numero != 0){
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un n�mero distinto de cero para sumar o cero para salir"));
        suma+=numero;
    }
    
    return suma;
  }
  
 
}
