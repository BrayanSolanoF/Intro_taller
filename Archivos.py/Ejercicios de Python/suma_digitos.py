# Dado un numero, sume los digitos
#Entrada: un numero entero
#Restricciones: es un entero positivo mayor a cero
#Salida: resultado de la suma
def suma_digitos(num):
    if isinstance(num,int)and(num>0):
        return suma_digitos_aux(abs(num))
    else:
        return "Error"
def suma_digitos_aux(num):
    if(num==0): #Condicion de parada
        return 0
    else: #Continuar
        return num%10 + suma_digitos_aux(num//10)
    
