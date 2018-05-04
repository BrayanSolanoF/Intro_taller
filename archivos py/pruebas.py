def agregar():
    base = open("prueba.txt", "at")
    
    print("Ingrese Id")
    ID=input()
    print("Ingrese nombre")
    nombre=input()
    print("Ingrese Correo")
    correo=input()
    print("Ingrese sitio web")
    sitio=input()
    lista = str(ID)+"$"+str(nombre)+"$"+str(correo)+"$"+str(sitio)+"$$"

    base.writelines(lista + "\n")

    base.close()

    
def leer():
    base = open("prueba.txt", "r")
    listado = base.readlines()
    base.close()
    
    return leer_aux(listado, 0)

def leer_aux(lista, cont):
    if cont == len(lista):
        return
    else:
        return [listar(lista[cont], 0)] + [leer_aux(lista, cont + 1)]

def listar(lis, cont):
    if cont == 4:
        return []
    else:
        return [lis.split("$")[cont]] + listar(lis, cont+1)
        
#[lista(listado[0], 0),lista(listado[1], 0)]
    
