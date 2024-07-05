class Customer:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def intro(self):
            print("My name is {} and my age is {}".format(self.name,self.age))
            
            
c1=Customer("shubham",24)
c2=Customer("ram",25) 
c3=Customer("shyam",26)

l=[c1,c2,c3]

for i in l:
     i.intro()
    
   
