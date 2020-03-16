from programs.exchange import currency_exchange

p = int(input('ingrese su cambio: '))
c = [50, 100, 200, 500, 1000]
x = []

currency_exchange.currencyExchange(p, c, x)

print(x)
