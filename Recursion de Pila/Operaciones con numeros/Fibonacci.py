def fibonacci (num):
  if isinstance (num,int) and (num>0):
    return fibonacci_aux(abs(num))
  else:
    return "Error"
    
def fibonacci_aux (num):
  if num==0:
    return 1 
  elif num == 1:
    return 1
  else:
    print (( num-1) + (num-2))
    return fibonacci_aux(num-1) + fibonacci_aux (num-2)