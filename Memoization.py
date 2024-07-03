def memo(num,d):
    if num in d:
        return d[num]
    else:
        d[num]=memo(num-1,d)+memo(num-2,d)#base Condition
        return d[num]
    


d={0:1,1:1}
print(memo(15,d))
print(d)

