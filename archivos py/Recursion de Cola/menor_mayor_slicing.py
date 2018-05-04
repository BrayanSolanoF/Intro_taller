def lista(lista):
    if isinstance(lista, list):
        print("El numero mayor de la lista es",mayor(lista,0))
        print("El numero menor de la lista es",menor(lista,0))
    else:
        return"Error"
def mayor(lista,resultado):
    if (lista==[] or len(lista) == 1):
        return resultado
    elif lista[0]>lista[1]:
        return mayor(lista[2:],lista[0])
    else:
        return mayor([lista[0]]+lista[2:],lista[1])

