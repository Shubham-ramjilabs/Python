l = ['AAPL', 'AAPL', 'Aapl', 'aapl', 'MSFT']
unique=set(l)
print(unique)

l2 = []
for symbol in l:
    l2.append(symbol.casefold())
print(l2)