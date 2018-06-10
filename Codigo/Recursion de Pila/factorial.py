#factorial
#Entradas:un numero
#Salidas:el factorial del numero
#Restricciones: un numero positivo
def factorial(num):
    if isinstance(num,int) and num>0:
        return factorial_aux(abs(num))
    else:
        "error"
def factorial_aux(num):
    if num == 0:
        return 1
    else:
        return num * factorial_aux(num-1)

print(factorial(5))
