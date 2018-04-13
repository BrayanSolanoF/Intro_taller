def decimal_fracciones(numero):
    if isinstance(numero, float):
       return  convertir_entero(int(numero)), convertir_fraccion(numero - int(numero))
    else: return "El valor no es un número real."
    
def convertir_entero(entero):
    if  isinstance(entero, int) and entero  > 0 or entero == 0:
        if entero == 1 or entero == 0:
            return [entero]
        else: return decimal_binario_aux(entero)
    else: return "Error: el valor ingresado no es un número."
    
def decimal_binario_aux(decimal):
    if decimal == 0: #rojo
        return []
    else: return decimal_binario_aux(decimal // 2) + [decimal % 2] # verde
    
def convertir_fraccion(fraccion):
    if isinstance(fraccion, float) and fraccion > 0:
        return fraccion_binario_aux(fraccion)
    else: return []
    
def fraccion_binario_aux(fraccion):
    if fraccion == 0.0: #rojo
        return []
    else: return  [ int(fraccion * 2)] + fraccion_binario_aux((fraccion * 2) - int(fraccion * 2)) # verde
