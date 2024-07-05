class Swimmer:
  def __init__(self, name):
    self.name = name

  def swim(self):
    print("Swimming...")

class Flyer:
  def __init__(self, name):
    self.name = name

  def fly(self):
    print("Flying...")

class Duck(Swimmer, Flyer):  # Inherits from both Swimmer and Flyer
  def __init__(self, name):
    super().__init__(name)  # Call the first parent class constructor (depends on method resolution order)

  def identify(self):
    print("I am a duck!")

d=Duck("Donald")
d.swim()
d.fly()
d.identify()