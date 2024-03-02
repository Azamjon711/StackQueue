class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        # self.items.insert(0, item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Error!!!")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Error!!!")

    def size(self):
        return len(self.items)


stack = Stack()

# print(stack.items)

stack.push(1)
stack.push(2)
stack.push(3)
# print(stack.items)

# stack.pop()
# print(stack.items)

# stack.peek()
# print(stack.peek())

# print(stack.size())


