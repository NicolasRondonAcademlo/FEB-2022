from multiplicar.operation import multiplicar
from resta.operation import resta
from suma.operation import suma
class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def suma(self):
        return suma(self.a, self.b)

    def resta(self):
        return resta(self.a, self.b)

    def multiplicar(self):
        return  multiplicar(self.a, self.b)


obj_1 = Calculator(2,5)
print(obj_1.suma())
print(obj_1.multiplicar())
print(obj_1.resta())