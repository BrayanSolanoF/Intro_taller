def  igual(x,lista):
     if isinstance(lista,list) and isinstance(x,int):
          return igual_aux(x,lista,0,False,len(lista))
     else:
          return "Error"

def igual_aux(x,lista,indice,valor,longitud):
     if indice==longitud:
          return valor
     else:
          if lista[indice]==x:
               return igual_aux(x,lista,indice+1,True,longitud)
          else:
               return igual_aux(x,lista,indice+1,valor,longitud)
