def sumaArray(lista):
     if isinstance(lista,list) and (lista!=[]):
          return suma(lista,0)
     else:
          "Error"
def suma(lista,result):
     for i in range (len(lista)):
          result+=lista[i]

     return result
          
