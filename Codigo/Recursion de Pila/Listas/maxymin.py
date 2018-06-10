def maxmin(lista):
     if isinstance(lista,list):
          return "Máximo :", minimo(lista),"Mínimo :",maximo(lista)
     else:
          return "Error"
def minimo(lista):
     if len(lista)==1:
          return lista[0]
     else:
          if lista[0]<lista[1]:
               return minimo([lista[0]]+lista[2:])
          else:
               return minimo(lista[1:])

def maximo(lista):
     if len(lista)==1:
          return lista[0]
     else:
          if lista[0]>lista[1]:
               return maximo([lista[0]]+lista[2:])
          else:
               return maximo(lista[1:])

