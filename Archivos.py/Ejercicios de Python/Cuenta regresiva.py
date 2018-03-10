def cuenta_regresiva(valor):
 print(valor)
 if (valor > 0): #Seguir-Verde
   cuenta_regresiva(valor - 1)
 else:

       if (valor<=0): #Parar- rojo
         return 0
