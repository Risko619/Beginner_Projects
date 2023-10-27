" In this project we create classes to model data and behaviours of our favorite pets, by using OOP to create flexible and efficient code"

# This is the parent class
class Pet:
  def __init__(self, pet_type, name, sound):
    self.pet_type = pet_type
    self.name = name
    self.sound = sound

  def speak(self):
    print(f"{self.name} goes {self.sound}!")

  def play(self):
    print(f"{self.name} is playing!")

# We'll use OOP inheritance to create a subclass of Pet() called cat
class Cat(Pet):
# this is called a 'constructor method' (line 19)
  def __init__(self, name, sound, coat_length):
# Because we're adding a new property which isn't in the parent class, we do the following superclass method.
    super().__init__("cat", name, sound)
    self.coat_length = coat_length

# Here I want to add a unique method only for Cat() objects, called purr.
  def purr(self):
    print(f"{self.name} is purring")

# This is an inheritance that creates another subclass of Pet(), called Dog.
class Dog(Pet):
  def __init__(self, name, sound, size):
    super().__init__("dog", name, sound)
    self.size = size

# For example of OOP polymorphism, we'll override the speak() method within the Dog() subclass in order to include the dog's size.
  def speak(self):
    print(f"{self.name} the {self.size} dog goes {self.sound}")

# Unique method for objects instantiated using Dog() class, called wag_tail.
  def wag_tail(self):
    print(f"{self.name} is wagging its tail")

# Below we test out or parent class (or superclass)
my_pet = Pet("gecko", "Sammy", "gek")
my_pet.speak()

# Testing our new Cat() subclass by creating an instance
cat = Cat("Mittens", "Meow", "long")
cat.purr()
cat.speak()
cat.play()
print(cat.coat_length)

# Testing our new Cat() subclass by creating an instance
dog = Dog("Cruiser", "Woof", "small")
dog.speak()
dog.wag_tail()
dog.play()
print(dog.size)

# Experiment
"""Add additional properties and methods to any of the existing classes.
Add additional subclasses to inherit from Cat() and/or Dog(). For example, create a Poodle() subclass that inherits from Dog() and encapsulates properties and methods unique to poodles.
Add validation/error handling for property values or method parameters. For example, write code to ensure that the pet's name is a non-empty string.
Practice overriding additional superclass methods within subclasses."""