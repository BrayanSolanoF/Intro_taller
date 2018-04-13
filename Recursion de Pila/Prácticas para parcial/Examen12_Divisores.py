def divisores(numero):
    if  isinstance(numero, int):
        if numero == 0 or numero == 1:
            return []
        elif numero == 2 or numero == 3:
                return []
        else:
            return divisores_aux(numero, 2)
    else: return "Error: el valor ingresado no es un número."

def divisores_aux(numero, contador):
    if  contador == numero: # Rojo
        return []
    elif numero % contador == 0: # Verde
            return [contador] + divisores_aux(numero, contador + 1) 
    else: return divisores_aux(numero, contador + 1) 
