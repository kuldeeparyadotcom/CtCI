class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


a = Stack() #Create an empty stack
print(a)
print(a.isEmpty()) #Check if stack is empty
a.push(2)
print(a.items)
a.push(3)
print(a.items)
print(a.peek())
print(a.pop())
print(a.items)
print(a.isEmpty()) #Check if stack is empty
