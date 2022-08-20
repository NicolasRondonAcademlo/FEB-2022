
class MyStack:
    def __init__(self) -> None:
        self.stack_list = []

    def is_empty(self):
        return len(self.stack_list) ==0
    
    def top(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)
    
    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()

class MaxStack:
    def __init__(self) -> None:
        self.max_stack = MyStack()
        self.main_stack = MyStack()

    def pop(self):
        self.max_stack.pop()
        return self.main_stack.pop()

    def push(self, value):
        self.main_stack.push(value)
        if self.max_stack.is_empty() or self.max_stack.top() < value:
            self.max_stack.push(value)
        else:
            self.max_stack.push(self.max_stack.top())
    
    def max_rating(self):
        if not self.max_stack.is_empty():
            return self.max_stack.top()


ratings = MaxStack()
ratings.push(5)
ratings.push(0)
ratings.push(2)
ratings.push(4)
ratings.push(6)
ratings.push(3)
ratings.push(10)

print(ratings.main_stack.stack_list)
print("MAximo puntaje " +  str(ratings.max_rating()))
ratings.pop()
ratings.pop()
ratings.pop()
print(ratings.main_stack.stack_list)
print("MAximo puntaje " +  str(ratings.max_rating()))