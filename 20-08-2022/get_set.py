# class User:
#     def __init__(self, username=None) -> None:
#         self.__username = username
    
#     def set_username(self,x):
#         self.__username = x
    
#     def get_username(self):
#         return self.__username

# steve = User("steve 1")

# print("Antes de setear", steve.get_username())
# steve.set_username("Steve 2")
# print("Despues de setear", steve.get_username())

# class User:
#     def __init__(self, username=None) -> None:
#         self.__username = username
    
#     @property
#     def username(self):
#         return self.__username

#     @username.setter
#     def username(self, value):
#         self.__username =value

# steve = User("steve 1")
# print(steve.username)
# steve.username = "Steve 5"
# print(steve.username)

class User:
    def __init__(self, username=None, password=None) -> None:
        self.username = username
        self.password = password
    
    def login(self, username, password):
        if self.username.lower() == username.lower() and self.password == password:
            return "Success Login"
        else:
            return ("Invalid Credentials")

# juan = User("juan", "12345")
# print(juan.login("juan", "12345"))
# print(juan.login("juan", "123456"))
# juan.password = "123456"
# print(juan.login("juan", "123456"))

class User:
    def __init__(self, username=None, password=None) -> None:
        self.__username = username
        self.__password = password

    @property
    def password(self):
        return self.__password.upper()
    
    @password.setter
    def password(self, password):
        "Toda la logica para cambiar la passwod"
        self.__password = password

    def login(self, username, password):
        if self.__username.lower() == username.lower() and self.__password == password:
            return "Success Login"
        else:
            return ("Invalid Credentials")

juan = User("juan", "12345")
print(juan.login("juan", "12345"))
print(juan.login("juan", "123456"))
juan.password = "123456a"
print(juan.password)
print(juan.login("juan", "123456a"))
