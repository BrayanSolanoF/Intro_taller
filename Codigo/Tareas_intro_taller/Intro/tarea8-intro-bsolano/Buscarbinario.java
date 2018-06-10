import javax.swing.JOptionPane;

public class Buscarbinario
{
  public static void main(String args[])
  {
    int lista[]=llenarArray();
    int valor = Integer.parseInt(JOptionPane.showInputDialog("Digite el numero: "));
    boolean encontrado = buscar(lista,valor);
    if(encontrado == true){
        JOptionPane.showMessageDialog(null,"Valor encontrado: "+ encontrado);
    }
    else{
        JOptionPane.showMessageDialog(null,"El valor no fue encontrado "+ encontrado);
    }
   

  }
  
  public static int[] llenarArray()
  {
    int lista[];
    int tamanio, valor=0;
    tamanio=Integer.parseInt(JOptionPane.showInputDialog("Digite la longitud de la lista: "));
    lista=new int[tamanio];
    for (int contador=0;contador<tamanio;contador++)
    {
      valor=Integer.parseInt(JOptionPane.showInputDialog("Digite los valores ordenados: "));
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