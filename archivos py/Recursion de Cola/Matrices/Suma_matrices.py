# suma el elemento con cada elemento de las filas
def suma_matriz(elemento,matriz):
    if isinstance(matriz, list) and matriz !=[] and isinstance(elemento, int):
        return matriz_aux(elemento, matriz, len(matriz), len(matriz[0]), 0, 0, [], [])
    else: return "La matriz no es una lista."
def matriz_aux(elemento, matriz, num_filas, num_columnas, fila, columna, suma, f):
    if fila == num_filas:
        return suma
    elif columna == num_columnas:
        return matriz_aux(elemento, matriz, num_filas, num_columnas, fila + 1, 0, suma + f, [])
    else: return (matriz_aux(elemento, matriz, num_filas, num_columnas, fila, columna + 1, suma, f + [matriz[fila][columna] + elemento]))
