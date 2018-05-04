def pares_impares(num):
    if isinstance(num, int):
        pares = lambda digito : digito % 2 == 0
        impares = lambda digito : digito % 2 == 1
        return pares_impares_aux(num, pares),pares_impares_aux(num, impares)
    else: return "Error"
def revise_aux(num,condicion):
    if num == 0:
        return 0
    elif condicion(num%10):
        return 1 + revise_aux(num // 10,condicion)
    else: return revise_aux(num // 10,condicion)
