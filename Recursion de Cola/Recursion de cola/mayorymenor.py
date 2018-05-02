def mayor(lista):
     if isinstance(lista,list):
          print("El mayor es: " ,may(lista,lista[0]))
          print("El menor es: ",men(lista,lista[0]))
     else:
          return "Error"

def may(lista,mayor):
     if lista==[]:
          return mayor
     else:
          if mayor<lista[0]:
               return may(lista[1:],lista[1])
          else:
               return may(lista[1:],mayor)

def men(lista,menor):
     if lista==[]:
          return menor
     else:
          if menor>lista[0]:
               return men(lista[1:],lista[1])
          else:
               return men(lista[1:],menor)



