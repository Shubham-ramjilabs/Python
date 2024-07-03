class Atm:
    def __init__(self):

        self.__balance=0
        self.__pin=""
        self.menu()
     
    def get_pin(self):
        return self.__balance
    
    def set_pin(self,new_pin):
        if type(new_pin)==str:
            self.__pin=new_pin  
        else:
            print("Invalid pin")



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
        self.__pin=int(input("Enter your pin: "))
        print("Pin set successfully")
        self.menu()


    def deposit(self):
        temp=int(input("Enter your pin: "))
        if temp==self.__pin:
            amount=int(input("Enter amount to deposit: "))
            self.__balance+=amount
            print("Amount deposited successfully")
        else:
            print("Invalid pin")

        self.menu()


    def withdraw(self):
        temp=int(input("Enter your pin: "))
        if temp==self.__pin:
            amount=int(input("Enter amount to withdraw: "))
            if amount<=self.__balance:
                self.__balance-=amount
                print("Amount withdrawn successfully")
            else:
                print("Insufficient balance")
        else:
            print("Invalid pin")

        self.menu()

    def check_balance(self):
        temp=int(input("Enter your pin: "))
        if temp==self.__pin:
            print("Balance: ",self.__balance)
        else:
            print("Invalid pin")

        self.menu()


sbi=Atm()
sbi.get_pin()
sbi.set_pin()

