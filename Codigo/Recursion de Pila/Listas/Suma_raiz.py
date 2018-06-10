#Sumar las raices de los numero de una lista
def raiz(lista):
     if isinstance(lista,list):
          return r(lista)
     else:
          return "Error"
def r(lista):
     if lista==[]:
          return 0
     else:
         return lista[0]**(1/2)+r(lista[1:])
