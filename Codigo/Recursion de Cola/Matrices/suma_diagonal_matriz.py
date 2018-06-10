#suma la diagonal de una matriz 
def suma_diagonal(matriz):
    if (isinstance(matriz,list) and matriz !=[] and len(matriz) == len(matriz[0])):
        return diagonal_aux(matriz, len(matriz), 0, 0)
    else: return "Error."
def diagonal_aux(matriz, filas, indice, suma):
    if indice == filas:
        return suma
    else: return(diagonal_aux(matriz, filas, suma + matriz[indice][indice], indice + 1))
