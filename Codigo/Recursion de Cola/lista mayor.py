def mayor(x,lista):
     if isinstance(lista,list) and isinstance(x,int)  :
          return may(x,lista,0,len(lista),0)
     else:
          return "Error"

def may(x,lista,indice,largo,res):
     if indice==largo:
          return res
     else:
          if x<lista[indice]:
               return may(x,lista,indice+1,largo,res+1)
          else:
               return may(x,lista,indice+1,largo,res)






