#Programa para determinar cuales numero son primos en una lista
def primos_list(lista):
    if isinstance (lista, list):
        return recorrer(lista)
    else:
        return "Error: el valor ingreado no es de tipo lista"

def recorrer(lista):
    if lista==[]:
        return []
    else:
        if primos_lista1(lista[0], lista[0]-1)==True:
            return [lista[0]] + recorrer(lista[1:])
        else:
            return recorrer(lista[1:])
def primos_lista1(lista,divisor):
    if isinstance(lista,int)and lista>=0 and divisor>=0 and isinstance(divisor,int):
        return primos_list_aux(lista, divisor)
    else:
        return "Error: los valores no son enteros positivos"
             
def primos_list_aux(lista,divisor):
    if (divisor==1) or (lista==1):
         return True
    elif ((lista % divisor) == 0):
          return False
    else:
          return primos_list_aux(lista, divisor -1)
