def iota(num):
    if isinstance(num, int) and num >0:
        return [iota_aux(num)]
    else:
        return "error"

def iota_aux(num):
    if num == 0:
        return 0 
    else:
        return num ,iota_aux(num-1)
    
