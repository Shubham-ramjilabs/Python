class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating instances of Dog and Cat
dog = Dog()
cat = Cat()

# Calling the speak method
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
