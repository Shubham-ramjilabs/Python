# d={"name":"shubham","age":24}
# print(d["name"])
# print(d["age"])
# d2={"name":"ram","collage":"NIT","Mark":{"M1":70,"py":85}}
# print(d2["Mark"]["py"])

class Atm:
    def __init__(self):

        self.balance=0
        self.pin=""
        self.menu()
     

    def menu(self):
        user_input=input("""
                                  Hi, Welcome to ATM
                                 1. Enter 1 to create pin
                                 2. Enter 2 to deposit
                                 3. Enter 3 to withdraw  
                                 4. Enter 4 to check balance
                                 5. Enter 5 to exit
    """)
    
        if user_input =="1":
            self.create_pin()

        elif user_input=="2": 
            self.deposit()

        elif user_input=="3":
            self.withdraw()

        elif user_input=="4":
            self.check_balance()

        else:
            print("Invalid input")

    def create_pin(self):
        self.pin=int(input("Enter your pin: "))
        print("Pin set successfully")


    def deposit(self):
        temp=input("Enter your pin: ")
        if temp==self.pin:
            amount=int(input("Enter amount to deposit: "))
            self.balance+=amount
            print("Amount deposited successfully")
        else:
            print("Invalid pin")

    def withdraw(self):
        temp=input("Enter your pin: ")
        if temp==self.pin:
            amount=int(input("Enter amount to withdraw: "))
            if amount<=self.balance:
                self.balance-=amount
                print("Amount withdrawn successfully")
            else:
                print("Insufficient balance")
        else:
            print("Invalid pin")


    def check_balance(self):
        temp=input("Enter your pin: ")
        if temp==self.pin:
            print("Balance: ",self.balance)
        else:
            print("Invalid pin")



sbi=Atm()