'''class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(self.year, self.make, self.model, "is starting...")

    def stop(self):
        print(self.year, self.make, self.model, "is stopping...")


car1 = Car("Honda", "Civic", 2020)
car1.start()
car1.stop()'''

class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def start(self):
        print(self.make,self.model,self.year,"is starting" )

    def stop(self):
        print(self.make,self.model,self.year,"is stopping" )       

car=Car("Swift","civic",2025)
car.start()
car.stop()
