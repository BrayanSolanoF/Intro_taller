def listapar(lista):
     if isinstance(lista,list):
          return listapar_aux(lista,len(lista),[],0)
     else:
          return "Error"

def listapar_aux(lista,lon,resultado,indice):
     if lon==indice:
          return resultado
     else:
          if lista[indice]%2==0:
               return listapar_aux(lista,lon,resultado+[lista[indice]],indice+1)
          else:
               return listapar_aux(lista,lon,resultado,indice+1)
