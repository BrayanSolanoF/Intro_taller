def busqueda(x,lista):
     if isinstance(lista,list) and isinstance(x,int):
          return busqueda_aux(x,lista,False,0,len(lista))
     else:
          return "Error"

def busqueda_aux(x,lista,valor,indice,lon):
     if indice==lon:
          return valor
     else:
          if lista[lon//2]>x:
               return busqueda_aux(x,lista,valor,indice,lon//2)
          if lista[lon//2]==x:
               return busqueda_aux(x,lista,True,indice,indice)
          if lista[lon//2]<x:
               return busqueda_aux(x,lista,valor,lon//2+1,lon+1)
