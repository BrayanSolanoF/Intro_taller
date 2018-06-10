def  igual(x,lista):
     if isinstance(lista,list) and isinstance(x,int):
          return igual_aux(x,lista,False)
     else:
          return "Error"

def igual_aux(x,lista,valor):
     if lista==[]:
          return valor
     else:
          if lista[0]==x:
               return igual_aux(x,lista[1:],True)
          else:
               return igual_aux(x,lista[1:],valor)
