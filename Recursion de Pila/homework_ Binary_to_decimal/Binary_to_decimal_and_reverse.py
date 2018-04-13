def binary_to_decimal(num):
    if isinstance(num, int):
        return binary_to_decimal_aux(num,0)
    else:"Error"
def binary_to_decimal_aux(num, exp):
    if num==0:
        return 0
    else:
        return ((num%10)*(2**exp))+ binary_to_decimal_aux(num//10,exp+1)

def decimal_to_binary(num):
    if isinstance(num, int):
        return decimal_to_binary_aux(num,0)
    else:"Error"

def len_binary_aux(num):
    if num==0:
        return 0
    else:
        return 1 + len_binary_aux(num//2)

def decimal_to_binary_aux(num,long):
    if num==0:
        return 0
    else:
        return ((num%2)*(10**long))+ decimal_to_binary_aux(num//2, long+1)
