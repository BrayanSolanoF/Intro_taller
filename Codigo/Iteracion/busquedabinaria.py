class Busquedabinaria:
    def __init__(self):
        pass
    def busquedabinaria(self,valor,lista):
        if isinstance(lista,list) and lista!=[]:
            return self.busqueda(lista,valor,False)
        else:
            return "Error"
    def busqueda(self,lista,valor,encontrar):
        for i in range (len(lista)):
            if valor==lista[(len(lista)-1)//2]:
                encontrar=True
            if valor<lista[(len(lista)-1)//2]:
                lista=lista[:(len(lista)-1)//2]
            else:
                lista=lista[(len(lista)-1)//2:]
        return encontrar
                
