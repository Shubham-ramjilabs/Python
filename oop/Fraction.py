class Fraction:
    def __init__(self,n,d):
        self.numerator=n
        self.denominator=d

    def __str__(self):
        return "{}/{}".format(self.numerator,self.denominator)
    
    def __add__(self,other):
        new_numerator=self.numerator*other.denominator+other.numerator*self.denominator
        new_denominator=self.denominator*other.denominator
        return "{}/{}".format(new_numerator,new_denominator)
    
    def __sub__(self,other):
        new_numerator=self.numerator*other.denominator-other.numerator*self.denominator
        new_denominator=self.denominator*other.denominator
        return "{}/{}".format(new_numerator,new_denominator)
    
    def __mul__(self,other):
        new_numerator=self.numerator*other.numerator
        new_denominator=self.denominator*other.denominator
        return "{}/{}".format(new_numerator,new_denominator)
    
    def __truediv__(self,other):    
        new_numerator=self.numerator*other.denominator
        new_denominator=self.denominator*other.numerator
        return "{}/{}".format(new_numerator,new_denominator)
    


x=Fraction(3,4)
y=Fraction(8,6)
print(x,y)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
