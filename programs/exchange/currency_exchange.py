def currencyExchange(p, c, x):
 act = 0
 j = len(c)-1
 for i in range(len(c)):
   x.append(0)
 while act != p:
   while (c[j] > (p-act)) and (j>0):
     j = j-1
   if j == 0:
     print("No existe solución")
   x[j] = int((p-act)/c[j])
   act = act + c[j]*x[j]
