class operaciones(object):
    def __init__(self):
        pass
   
    def binary_to_decimal(self,num):
        if isinstance(num, int):
            return self.binary_to_decimal_aux(num,0)
        else:"Error"
    def binary_to_decimal_aux(self,num,exp):
        if num==0:
            return 0
        else:
            return ((num%10)*(2**exp))+ self.binary_to_decimal_aux(num//10,exp+1)

    def decimal_to_binary(self,num):
        if isinstance(num, int):
            return self.decimal_to_binary_aux(num,0)
        else:"Error"

    def len_binary_aux(self,num):
        if num==0:
            return 0
        else:
            return 1 + self.len_binary_aux(num//2)

    def decimal_to_binary_aux(self,num,exp):
        if num==0:
            return 0
        else:
            return ((num%2)*(10**exp))+ self.decimal_to_binary_aux(num//2, exp+1)


x=operaciones()
print(x.decimal_to_binary(23))
