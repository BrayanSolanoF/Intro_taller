def min(lista):
     if isinstance(lista,list):
          return minimo(lista)
     else:
          return "Error"
def minimo(lista):
          if lista[0]<lista[1]:
               return minimo([lista[0]]+lista[2:])
          else:
               return minimo([lista[1:]])
