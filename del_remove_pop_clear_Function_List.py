l=[1,2,3,4,5,6,[7,8,9]]
#del
del l[0]
print(l)
del l[1:3]
print(l)

#remove
l.remove(6)
print(l)
l.remove([7,8,9])
print(l)
l.append([1,2,3,4,5])
print(l)

#pop
l.pop()
print(l)
l.pop(0)
print(l)

#clear
l.clear()
print(l)
