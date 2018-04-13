def intercambio(num):
    if isinstance(num, int):
        return intercambio_aux(num, 0)
    else: return 

def intercambio_aux(num, contador):
    if num == 0:
        return 0
    else: return ((((num // 10) % 10) * (10 ** contador))
                + ((num % 10)) * (10 ** (contador + 1))
                + intercambio_aux(num // 100, contador + 2))
