def sum_exponente(lista):
    if isinstance(lista, list):
        return sum_exponente_aux(lista,1)
    else: return "El objeto ingresado no es una lista."
def sum_exponente_aux(lista,exp):
    if lista ==[]:
        return 0
    elif isinstance(lista[0], list):
        #return sum_exponente_aux(lista[0],exp)+ sum_exponente_aux(lista[1:],exp + len(lista[0]))
        return sum_exponente_aux(lista[0] + lista[1:], exp)
    else: return lista[0]**(exp) + sum_exponente_aux(lista[1:], exp+1)
