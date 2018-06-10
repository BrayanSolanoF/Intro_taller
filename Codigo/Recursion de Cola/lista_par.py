#hacer una nueva lista con los digitos pares de una lista mediante indice

def lista_par(lista):
    if isinstance(lista,list):
        return lista_par_aux(lista,len(lista),[],0)
    else:
        return"Error"
def lista_par_aux(lista,largo,resultado,indice):
    if indice==largo:
        return resultado
    elif(lista[indice]%2)==0:
        return lista_par_aux(lista,largo,resultado+[lista[indice]],indice + 1)
    else:
        return lista_par_aux(lista,largo,resultado,indice+1)
