
class Animal:
    def __init__(self,name):
        self.name=name

    def eat(self):
        print(self.name,"is eating")    

class Dog(Animal):
    def bark(self):
        print(self.name,"is barking")

class Cat(Animal):
    def meow(self):
        print(self.name,"is meowing")        

dog=Dog("Tommy")
dog.eat()
dog.bark()

cat=Cat("Jerry")
cat.eat()
cat.meow()