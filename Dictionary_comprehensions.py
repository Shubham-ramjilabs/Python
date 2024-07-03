d={"name":"shubham","age":24,"city":"pune"}
d1={key:value for key,value in d.items() if len(key)>3}
print(d1)

d2=[1,2,3,4,5,6]
d3={x:x**2 for x in d2}
print(d3)

d3={x:x**2 for x in d2 if x%2==0}
print(d3)