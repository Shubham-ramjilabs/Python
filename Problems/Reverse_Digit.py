num=1234
l=''
l=num
l1=[]
rev=0
while num!=0:
    rem=num%10  
    rev=rev*10+rem
    num=num//10


l1=rev

print(rev)
while rev!=0:
    rem=rev%10
    num=num*10+rem
    rev=rev//10
print(num)
print(l1)


# check the reverse number is true or not
if str(num)==str(l):
    print(True)
else:
    print(False)
