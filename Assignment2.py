#input=how are you
#Out put= How Are You
str="how are you"
print(str.split(" "))
str1=[]
for i in str.split(" "):
    str1.append(i.capitalize())

print(" ".join(str1))


