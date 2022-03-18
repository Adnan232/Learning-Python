class Car:
    def __init__(self, name, color):
        self.name=name
        self.color=color
    def des_car(self):
        print ("Car:", self.color, self.name)
car1 = Car("Maruti", "brown")
car1.des_car()
car2 = Car("Toyota", "black")
car2.des_car()
