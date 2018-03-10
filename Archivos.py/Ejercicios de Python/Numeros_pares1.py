def Numeros_menores_cuatro(num):
  if isinstance (num, int) and (num > 0):
    return Numeros_menores_cuatro(num)
  else:
    return "Error"
def numeros_menores_cuatro(num):
  if(num==0): #Condicion de parada
     return True
  else:
    if num%10>=0 and num%10<=4:
      return numeros_menores_cuatro(num // 10)
    else:
      return False
  

