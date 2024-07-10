s='FfEeDdCcBbAa'
l=''
u=''
for i in s:
    if i.islower():
        l=l+i
    else:
        u=u+i

print(l[::-1])
print(u[::-1])

