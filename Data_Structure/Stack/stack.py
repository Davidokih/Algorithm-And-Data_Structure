
class Stack():
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items = self.items + [element]

    def pop(self):
        return self.items.pop()

    def peek(self):
        count = len(self.items)
        if (self.items == 0):
            return

        return self.items[count - 1]

    def print(self):
        print(self.items)


stack = Stack()

stack.push(10)
stack.push(14)
stack.push(20)

stack.print()
