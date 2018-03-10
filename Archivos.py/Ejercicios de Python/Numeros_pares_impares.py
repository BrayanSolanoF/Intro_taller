def Numeros_pares_impares(num):
  if isinstance (num, int) and (num > 0):
    print ("Numeros pares:",Numeros_pares(num),"Numeros impares:",Numeros_impares(num))
  else:
    return "Error"
def Numeros_pares(num):
  if(num==0): #Condicion de parada
     return 0
  else:
    if ((num%10)%2)==0:
      return 1+ Numeros_pares(num // 10)
    else:
      return Numeros_pares(num // 10)
def Numeros_impares(num):
  if(num==0): #Condicion de parada
     return 0
  else:
    if ((num%10)%2)==0:
      return  Numeros_impares(num // 10)
    else:
      return 1+ Numeros_impares(num // 10)
  
  
