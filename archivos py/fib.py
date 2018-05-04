from time import *

def fib(n):
    if isinstance(n, int) and n>=0 :
        n=abs(n)
        if n==0:
            return 1
        else:
            return fib_aux(n-1)
    else:
        return "Error"

    
def fib_aux(n, a=1, b=0, cont=1):
    if n==1:
        return a+b, cont
    else:
        fib=a+b
        b=a
        a=fib
        return fib_aux(n-1,a,b, cont + 1)



def fib_pila(n):
    global tiempo1
    tiempo1 = time()
    if isinstance(n,int):
        
        return fib_pila_aux(n)
    else:
        return "Error"
cont = 1
def fib_pila_aux(n):
    global cont
    cont += 1
    if n==0:
        print(cont)
        print(tiempo1-time())
        return 0
    elif n==1:
        return 1
    else:
        return fib_pila_aux(n-1) + fib_pila_aux(n-2)

