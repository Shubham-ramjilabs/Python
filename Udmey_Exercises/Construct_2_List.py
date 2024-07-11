d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'d': 100, 'e': 200, 'f': 300}
d3 = {'f': 30, 'g': 40}
key=[]
value=[]

for i in d1:
    key.append(i)
for i in d1:
    value.append(d1[i])
for i in d2:
    key.append(i)
for i in d2:
    value.append(d2[i])
for i in d3:
    key.append(i)
for i in d3:
    value.append(d3[i])
print(key)
print(value)


keys=[]
values=[]
for d in (d1, d2, d3):
    for key, value in d.items():
        keys.append(key)
        values.append(value)



        