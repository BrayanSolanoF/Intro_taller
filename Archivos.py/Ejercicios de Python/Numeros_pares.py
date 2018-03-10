#Dado un numero, determine la longitud (numero de digitos)
#Entrada: es un numero entero
#Restricciones: es un entero positivo mayor a cero
#Salida: longitud de un numero
def Numeros_pares(num):
  if isinstance (num, int) and (num > 0):
    return Numeros_pares_aux(num)
  else:
    return "Error"
def Numeros_pares_aux(num):
  if(num==0):
     return 0
  else:
    if ((num%10)%2)==0:
      return 1+ Numeros_pares_aux(num)
    else:
      return Numeros_pares_aux(num)
  
