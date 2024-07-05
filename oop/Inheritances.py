class User:#parent class
    def login(self):
        print("User logged in")


    def register(self):
        print("User registered")
    

class Strudent(User):#child class we inherit from parent class
    def enroll(self):
        print("Student enrolled")

    def review(self):
        print("Student reviewed")

s1=Strudent()
s1.login()
s1.register()
s1.enroll()
s1.review()