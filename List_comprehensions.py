l=[x **2 for x in range(1,11)]#squar root
print(l)

l1=[x for x in range(1,11)if x%2==0]
print(l1)

furit=["apple","banana","mango","orange"]
l2=[furit for furit in furit if furit[0]=="a"]
print(l2)

String="Python is a awesome language".split(" ")
l3=[x for x in String if len(x)>=5]
print(l3)
