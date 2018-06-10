def invertir(num):
    if isinstance(num, int):
        return invertir_aux(num,0)
    else:
        return "Error."
def invertir_aux(num,exp):
    if (num == 0):
        return 0
    else:
        return((num%10)*(10**(exp+1)))+((num%100)//10)*(10**exp)+ invertir_aux((num//100), exp+2)
                
          
