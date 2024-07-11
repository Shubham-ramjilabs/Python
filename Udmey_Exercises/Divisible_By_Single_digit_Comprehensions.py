result=[]
for number in range(1,101):
    for div in range(2,11,2):
        if number%div==0:
            result.append(number)
            break
not_divisible = set(range(1, 100)) - set(result)
print(not_divisible)
