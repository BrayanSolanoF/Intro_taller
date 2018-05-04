def positivos (lista):
    if isinstance(lista,list):
        positivo = lambda digito : digito < 0
        return positivos_aux(lista, positivo)
    else: return "Error"
def positivos_aux(lista,condicion):
    if lista == []:
        return True
    elif condicion(lista[0]):
        return False
    else: return positivos_aux(lista[1:], condicion) #verde

