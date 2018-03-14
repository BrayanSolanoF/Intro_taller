def productoria(num):
  if isinstance (num,int) and (num>0):
    return productoria_aux(abs(num))
  else:
    return "Error"
  def productoria_aux (num):
    if (num==0):
      return 1
    else:
      return (3*num-2)*productoria_aux(num-1)