# ejercicio 1
def iota(num):
    if isinstance(num, int) and num>0:
        return iota_aux(num)
    else:
        return "error"

def iota_aux(num):
    if num == []:
        return 0
    else:
        return 1 + suma_aux(lista[1:])
