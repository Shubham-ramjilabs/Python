class Parent:
    def __init__(self,num):
        self.num=num
    def get_num(self):
        return self.num
class child(Parent):
    def __init__(self,num,val):
        super().__init__(num)
        self.val=val
    def get_val(self):
        return self.val
    

c=child(5,6)

print(c.get_val())  
print(c.get_num())
