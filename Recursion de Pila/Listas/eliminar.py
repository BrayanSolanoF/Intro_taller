#Hacer una funcion quer indique si todos los elementos de una lista son positivos
def eliminar (lista, numero):
    if isinstance (lista, list):
        return lista_aux(lista, numero)
    else: return "Error"
def lista_aux(lista,numero):
    if lista==[]:
        return []
    else:
        if lista[0]==numero:
            return lista_aux(lista[1:], numero)
        else:
            return [lista[0]]+ lista_aux(lista[1:], numero)
