def eliminar_divisibles(num):
    if isinstance(num,int):
        return eliminar_divisibles_aux(num,0,0)
    else:
        return "El numero no es un entero"
def eliminar_divisibles_aux(num,resultado,contador):
    if(num==0):
        return resultado
    elif ((num%10)%3)!=0:
        return eliminar_divisibles_aux((num//10),(num%10)*(10**contador)+ resultado, contador+1)
    else:
        return eliminar_divisibles_aux((num//10), resultado, contador)
