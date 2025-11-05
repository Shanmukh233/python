# Base class
class Animal:
    def make_sound(self):
        print("Some generic animal sound")

# Derived classes
class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class Bird(Animal):
    def make_sound(self):
        print("Chirp!")

animals = [Dog(), Cat(), Bird()]

for a in animals:
    a.make_sound()  
