#Suma todos los numeros pares de una lista
def suma_pares(lista):
    #if type(lista) == list
    if isinstance (lista, list):
        return suma_pares_aux(lista)
    else: return "Error: el valor ingresado no es una lista."

def suma_pares_aux(lista):
    if lista == []:
        return 0
    else:
        if (lista[0]%2)==0:
            return lista[0]+suma_pares_aux(lista[1:])
        else:
            return suma_pares_aux(lista[1:])
