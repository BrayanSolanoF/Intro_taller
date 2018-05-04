def iota(num):
    if isinstance(num, int) and num >0:
        return [iota_aux(num,0)]
    else:
        return "error"

def iota_aux(num,cont):
    if num -1== cont:
        return cont  
    else:
        return cont,iota_aux(num,cont+1)
    
#Está malo. Revise :v
def iotaChecked(num):
    if isinstance(num, int) and num > 0:
        return iota_auxChecked(num, [])
    else:
        return "Error, el dato ingresado no es un número positivo"

def iota_auxChecked(num,lista):
    if num == 0:
        return lista;
    else:
        return iota_auxChecked(num - 1, [num] + lista)
    
    
