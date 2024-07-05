class Animal:
  def __init__(self, name):
    self.name = name

  def make_sound(self):
    print("Generic animal sound")

class Mammal(Animal):
  def __init__(self, name, fur_color):
    super().__init__(name)
    self.fur_color = fur_color

class Dog(Mammal):
  def __init__(self, name, breed, fur_color):
    super().__init__(name, fur_color)
    self.breed = breed

  def make_sound(self):
    print("Woof!")

# Creating an instance of Dog
dog=Dog("Buddy", "Labrador", "brown")
print(dog.name)  # Output: Buddy
print(dog.breed)  # Output: Labrador
print(dog.fur_color)  # Output: brown
dog.make_sound()  # Output: Woof!