class Stack():
    def __init__(self):
        self.items = []
    
    def push(self , element):
       for i in range(0, len(self.items) + 1):
           return self.items + element
    def print(self):
        print(self.items)

stack = Stack()

stack.push(10)
stack.push(14)
stack.push(20)

stack.print()