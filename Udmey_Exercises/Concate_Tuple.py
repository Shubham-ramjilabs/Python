t1 = 1, 2, 3, 4, 5, 6
t2 = 7, 8, 9, 10
t3 = 11, 12, 13, 14, 15, 16, 17
l1=list(t1)
l2=list(t2)
l3=list(t3)

l1[::2]=[0,0,0]
l2[::2]=[0,0]
l3[::2]=[0,0,0,0]
l=l1+l2+l3
print(l)



    


    