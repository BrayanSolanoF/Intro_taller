def summ(n):
    if isinstance(n, int):
        return summ_aux(n, 0)
    else:
        return "Error"

def mul_aux(j, z):
    if z == j + 1:
        return 1
    else: return ((3 * z ** 2) - z) * mul_aux(j, z + 1)

def summ_aux(n, j):
    if j == n:
        return 0
    else: return mul_aux(j + 1, 1) + summ_aux(n, j + 1)
