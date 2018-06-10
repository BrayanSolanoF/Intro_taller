#suma la diagonal de una matriz 
def suma_antidiagonal(matriz):
    if isinstance(matriz,list) and matriz !=[] and len(matriz) == len(matriz[0]):
        return antidiagonal_aux(matriz, len(matriz), 0, 0)
    else: return "Error."
def diagonal_aux(matriz, largo, fila, suma):
    if filas == largo:
        return suma
    else: return(antidiagonal_aux(matriz, largo, fila + 1, suma + matriz[fila][-(fila + 1)])
