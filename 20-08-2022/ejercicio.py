subjects = ["phy", "chem", "bio"]
max_score = 300
class Student:
    def __init__(self, name, phy, chem, bio):
        if bio > 100 or phy  > 100 or chem   > 100:
            raise Exception("El maximo puntaje por materia es 100")
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def total_obtained(self):
        return self.bio + self.phy + self.chem

    def percentage(self):
        return int((self.total_obtained()/300) *100)

maria = Student("maria", 80,50,99)
print(maria.total_obtained())
print(maria.percentage())