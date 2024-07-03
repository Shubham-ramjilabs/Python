l=[1,2,4,5,6,7,8]
t=list(map(lambda x:x*2,l))
print(t)

x=list(map(lambda x: x%2==0,l))
print(x)

students=[
    {
        "name":"shubham",
        "age":24

    },
    {
        "name":"ram",
        "age":25
    },
    {
        "name":"shyam",
        "age":26
    }

]
y=list(map(lambda student: student["name"],students))
print(y)