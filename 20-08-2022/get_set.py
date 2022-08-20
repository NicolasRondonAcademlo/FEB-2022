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

class User:
    def __init__(self, username=None) -> None:
        self.__username = username
    
    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username =value

steve = User("steve 1")
print(steve.username)
steve.username = "Steve 5"
print(steve.username)