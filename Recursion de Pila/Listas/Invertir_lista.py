def invertir(lista):
    if isinstance(lista,list):
        return invertir_aux(lista)
    else:
        return"Error: el vlaor ingresado no es una lista"

def invertir_aux(lista):
    if lista == []:
        return []
    else:
        return [lista[-1]]+ invertir_aux(lista[:-1])
