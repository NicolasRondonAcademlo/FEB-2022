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

class Player:
    team_name = " Liverpool"
    def __init__(self, name) -> None:
        self.name = name

p1 = Player("Mark")
p2 = Player("Steve")
print("Name", p1.name)
print("Team", p1.team_name)

print("Name", p2.name)
print("Team", p2.team_name)