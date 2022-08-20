# Un objeto es algo que tiene comportamientos y datos
# -> Metodos y tiene propiedades

class MyClassName:
    pass

#class Employee:
#    ID = None
#    salary = None
#    department = None
    
# class Employee:
#     ID = 2879
#     salary = 2500
#     department = "Human Resources"

# steve = Employee()
# print(steve.ID)
# print(steve.salary)
# print(steve.department)
# steve.ID = 7899
# steve.salary = 455
# steve.department = "Tech"
# print("---")
# print(steve.ID)
# print(steve.salary)
# print(steve.department)
# steve.rol = "Tech Lead"
# print(steve.rol)

# Crea -> Inicializa ->Destroy

# class Employee:
#     def __init__(self, ID, salary, department) -> None:
#         self.ID = ID
#         self.salary = salary
#         self.department = department
    

# steve = Employee(7, 5488, "Marketing")
# print(steve.ID)
# print(steve.salary)
# print(steve.department)
# lucy = Employee(1, 54880, "CEO")
# print(lucy.ID)
# print(lucy.salary)
# print(lucy.department)


# class Employee:
#     def __init__(self, ID=None, salary=0, department=None) -> None:
#         self.ID = ID
#         self.salary = salary
#         self.department = department
# alex = Employee()

# class Player:
#     team_name = " Liverpool"
#     def __init__(self, name) -> None:
#         self.name = name

# p1 = Player("Mark")
# p2 = Player("Steve")
# print("Name", p1.name)
# print("Team", p1.team_name)

# print("Name", p2.name)
# print("Team", p2.team_name)

# class Employee:
#     def __init__(self, ID=None, salary=None, department=None):
#         self.ID = ID
#         self.salary = salary
#         self.department = department
    
#     def tax(self):
#         return self.salary * 0.2
    
#     def salary_per_day(self):
#         return self.salary / 30
    



# steve = Employee(2387, 4800, "Operations")
# print(steve.salary)
# print(steve.tax())
# print(steve.salary_per_day())

# class Doctor:
#     def __init__(self,
#                 name, 
#                 hospital,
#                 university,
#                 speciality
#       ) -> None:
#         self.name = name
#         self.speciality =speciality
#         self.university = university
#         self.hospital = hospital
    
#     def surgery(self):
#         return f"El medico {self.name} especialista en {self.speciality} esta operando en {self.hospital}"

#     def teaching(self):
#         return f"{self.name} da clases en {self.university} de {self.speciality}"

# pepito = Doctor(
#     "pepito",
#     "HIS",
#     "UIS",
#     "Cardiologia"
# )
# print(pepito.surgery())
# print(pepito.teaching())

# class Player:
#     team_name = "Liverpool"
    
#     def __init__(self, name) -> None:
#         self.name = name

#     @classmethod
#     def get_team_name(cls):
#         return cls.team_name

#     @staticmethod
#     def demo():
#         return "Static mehtod"

# print(Player.get_team_name())
# print(Player.demo())

# def funcion_a(funcion_b):
#     def funcion_c():
#         print("Anbtes de la funcion")
#         funcion_b()
#         print("Despues de la funcion")
#     return funcion_c

# @funcion_a
# def saludar():
#     print("Hola Mundo")

# saludar()
class Employee:
    def __init__(self, ID=8, salary=984):
        self.ID = ID
        self.__salary = salary

# En python todoo es publico, podemos simular que algo es privado

a = Employee()

print(a.ID)
#print(a._Employee__salary)
print(a.__salary)
