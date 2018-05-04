def lista(lista):
    if isinstance(lista, list) and lista !=[]:
        print("El numero mayor de la lista es",mayor(lista,len(lista),0,1))
        print("El numero menor de la lista es",menor(lista, len(lista),0,1))
    else:
        return"Error"
def mayor(lista,largo,posicion1,posicion2):
    if posicion2==largo:
        return lista[posicion1]
    elif lista[posicion1]>lista[posicion2]:
        return mayor(lista,largo,posicion1,posicion2+1)
    else:
        return mayor(lista,largo,posicion2,posicion2+1)

def menor(lista,largo,posicion1,posicion2):
    if posicion2==largo:
        return lista[posicion1]
    elif lista[posicion1]<lista[posicion2]:
        return menor(lista,largo,posicion1,posicion2+1)
    else:
        return menor(lista,largo,posicion2,posicion2+1)
