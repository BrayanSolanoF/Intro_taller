def busqueda(x,lista):
     if isinstance(lista,list) and isinstance(x,int):
          return busqueda_aux(x,lista,len(lista)//2)
     else:
          return "Error"

def busqueda_aux(x,lista,valor):
     if lista==[]:
          return False
     else:
          if lista[valor]<x:
               return busqueda_aux(x,lista[(valor+1):], (len(lista[(valor+1):])-1)//2)
          if (lista[valor]==x):
               return True
          if lista[valor]>x:
               return busqueda_aux(x,lista[:valor], len(lista[:valor])//2)
