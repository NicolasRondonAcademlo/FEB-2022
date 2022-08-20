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

# maria = Student("maria", 80,50,99)
# print(maria.total_obtained())
# print(maria.percentage())
# Account - title, balance --- depositar, retirar, obtener balance
# SAvings - interest_rate
# Tener un metodo para saber la cantidad de intereses que ha gando mi cuenta

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
        
    def withdrawal(self, amount):
        self.balance = self.balance  -amount

    def deposit(self,amount):
        self.balance = self.balance + amount
    
    def get_balance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interest_rate):
        super().__init__(title,balance)
        # write your code here
        self.interest_rate = interest_rate

    def interest_amount(self):
        return self.balance* self.interest_rate /100

demo1 = SavingsAccount("Jorge", 2000, 5)
demo1.deposit(2000)
demo1.deposit(5000)
demo1.withdrawal(300)
print(demo1.interest_amount())