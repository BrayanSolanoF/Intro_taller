def validar(num):
  if isinstance (num, int) and (num > 1):
    return Numeros_primos (num, num-1)
  else:
    return "Numero especial"
def Numeros_primos(num, divisor):
    if (divisor==1):
         return True
    elif ((num % divisor) == 0):
          return False
    else:
          return Numeros_primos (num, divisor -1)

