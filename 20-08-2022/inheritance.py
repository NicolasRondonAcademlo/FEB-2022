class Vehicle:
    def __init__(self, make, color, model) -> None:
        self.make = make
        self.color =color
        self.model = model
    
    def print_details(self):
        print("Manufacturer: ", self.make)
        print("Color: ", self.color)
        print("Model: ", self.model)

class Car(Vehicle):
    def __init__(self, make, color, model, doors) -> None:
        super().__init__(make, color, model)
        self.doors = doors
        #Vehicle.__init__(self, make, color, model)
    
    def print_car_details(self):
        self.print_details()
        print("Doors: ",self.doors)
        
class OtherClass:
    pass
# Diamond Problem
# Mixin 




ob1 =  Car("Susuky", "Grey", "2015",4)
ob1.print_car_details()

class A:
    def saludar(self):
        print("Hola")


class B(A):
    def despedir(self):
        print("Adios")

objeto = B()
objeto.saludar()
objeto.despedir()