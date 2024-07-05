import sys
L=[x for x in range(1,10000)]
print(sys.getsizeof(L)/1024)

#using Iterator
x=range(1,10000)
print(sys.getsizeof(x)/1024)