def sum(fun,L):
    result=0
    for i in L:
        if fun(i):
         result=result+i
        
        
    return result






L=[11,25,52,30,50,19]
x=lambda x: x%2==0
y=lambda y:y%2!=0
z=lambda z:z%3==0

print(sum(x,L))
print(sum(y,L))
print(sum(z,L))
    