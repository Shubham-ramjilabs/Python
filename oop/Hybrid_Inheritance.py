class Animal:
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

class Bat(Mammal, Bird):
    def __init__(self, name):
        super().__init__(name)

# Creating an instance of Bat
bat = Bat("Bruce")
print(bat.name)  # Output: Bruce
