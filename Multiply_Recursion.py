def multiply(x,y):
    if y==0:
        return 0
    else:
        result= x+multiply(x,y-1)
        return result


x=int(input("Enter the First number"))
y=int(input("Enter the Second number"))
result=multiply(x,y)
print(result)
