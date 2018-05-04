def contiene_cero(lista):
    if isinstance(lista,list):
        cero = lambda digito : digito == 0
        return contiene_cero_aux(lista, cero)
    else: return "Error"
def contiene_cero_aux(lista,condicion):
    if lista == []:
        return False
    elif condicion(lista[0]):
        return True
    else: return contiene_cero_aux(lista[1:], condicion) #verde

    
