import functools
l=[1,2,3,45,5]
sum=functools.reduce(lambda x,y:x+y,l)
print(sum)

#max num
max=functools.reduce(lambda x,y:x if x>y else y,l)
print(max)

#min
min=functools.reduce(lambda x,y:x if x<y else y,l)
print(min)

#Flattening a List of Lists
l1=[[1,2,3],[4,5,6],[7,8,9]]
print(functools.reduce(lambda x,y:x+y,l1))

#Concatenating Strings
word=["hello"," ","world"]
print(functools.reduce(lambda x,y:x+y,word))