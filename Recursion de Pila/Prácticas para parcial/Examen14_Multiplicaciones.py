def multiplicaciones2(digi, num):
    if isinstance(num, int) and isinstance(digi, int) and num != 0 and digi > 0:
        return multi_aux2(digi, num)
    else:  return "El número no es un entero."

# Se requiere agregar código adicional para lograr la
# funcionalidad requerida.
def multi_aux2(digi, num):
    if num == 0:
        return []
    else:
        return (multi_aux2(digi, num // 10)  +
                [num % 10 * digi])
    
