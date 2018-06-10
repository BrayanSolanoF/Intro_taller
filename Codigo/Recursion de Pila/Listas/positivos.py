#Hacer una funcion quer indique si todos los elementos de una lista son positivos
def positivos (lista):
    if isinstance (lista, list):
        return positivo_aux(lista)
    else: return "Error"
def positivo_aux(lista):
    if lista==[]:
        return True
    else:
        if lista[0]<0:
            return False
        else:
            return positivo_aux(lista[1:])
