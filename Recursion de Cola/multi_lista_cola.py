def multi_lista(lista):
    if isinstance (lista,list):
        return multi_lista_aux(lista,1)
    else:
        return"El objeto no es una lista"
def multi_lista_aux(lista,resultado):
    if (lista==[]):
        return resultado
    elif isinstance (lista[0], list):
        return multi_lista_aux(lista[0]+lista[1:],resultado)
    else:
        return multi_lista_aux(lista[1:],lista[0]*resultado)
