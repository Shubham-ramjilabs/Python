class Area:
    def area(self,a,b=0):
        if b==0:
            print("Area of circle is",3.14*a*a)
        else:
            print("Area of rectangle is",a*b)   


a=Area()
a.area(5)
a.area(5,6)