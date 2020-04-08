from programs.exercise_voraz import currency_exchange, knapsack_problem, min_and_max
# Ejercicio del cambio de monedas, mediate un algoritmo voraz dice cuantas monedas debe regresar
print('############ Exercise exchange ############')
p = int(input('ingrese su cambio: '))
c = [50, 100, 200, 500, 1000]
x = []

currency_exchange.currencyExchange(p, c, x)
print(c)
print(x)

#Ejercicio de la mochila implementando un algoritmo voraz
print()
print('########### KnapSack Problem ############')
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print (knapsack_problem.knapSack(W , wt , val , n))

#Ejercicio de minimo y maximo voraz punto 6
print()
print('########### min and max number ############')
arr = [1000, 11, 445, 1, 330, 3000]
high = len(arr) - 1
low = 0
arr_max, arr_min = min_and_max.getMinMax(arr, len(arr))
print('Minimum element is ', arr_min)
print('nMaximum element is ', arr_max)
