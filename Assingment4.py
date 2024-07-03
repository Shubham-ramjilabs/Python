#remove duplicate elements from list
l=[1,1,2,2,3,4,5,6,6,7,10]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)

print(l1)