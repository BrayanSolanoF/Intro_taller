class Ingresarvalores:
    def __init__(self):
        pass
        
    def sumar(self):
        salir=True
        sumar1=0
    
        while salir:
            num=int(input("Introducir numeros, 0 para detener"))
            sumar1+=num
            if num==0:
                salir=False
        return sumar1
            
            
