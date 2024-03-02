class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Error!!!")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Error!!!")

    def size(self):
        return len(self.items)


queue = Queue()

print(queue.is_empty())