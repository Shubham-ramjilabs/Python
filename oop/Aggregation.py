class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address

    def edit(self,new_name,new_city,new_state,new_pincode):
        self.name=new_name
        self.address.change_address(new_city,new_state,new_pincode)


class Address:
    def __init__(self,city,state,pincode):
        self.city=city
        self.state=state
        self.pincode=pincode

    def change_address(self,new_city,new_state,new_pincode):
        self.city=new_city
        self.state=new_state
        self.pincode=new_pincode


add=Address("pune","maharashtra",411001)
cus=Customer("shubham","male",add)
cus.edit("shubham","mumbai","maharashtra",411001)
print(cus.address.city)
print(cus.address.pincode)