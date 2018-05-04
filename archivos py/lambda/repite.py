def repite(lista, num):
    if isinstance(lista,list) and isinstance (num, int) and (num > 0):
        rep = lambda digito : digito  == num
        return repite_aux(lista,rep)
    else: return "Error"
def repite_aux(lista,condicion):
    if lista == []:
        return 0
    elif condicion(lista[0]):
        return 1 + repite_aux(lista[1:],condicion)
    else: return repite_aux(lista[1:],condicion)
