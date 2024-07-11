data = {
    'd1': {'a': 1, 'b': 2, 'c': 3},
    'd2': {'b': 20, 'c': 30, 'd': 40},
    'd3': {'d': 100, 'x': 200}
}
#1 way
print(data['d1'].keys() | data['d2'].keys() | data['d3'].keys())
#way 2
result = set()
for d in data.values():
    result = result | d.keys()

print(result)