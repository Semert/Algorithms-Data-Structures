"""
Stack Data Structure.
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []  # True or False

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Sondaki elemanı verir.

    def get_stack(self):
        return self.items


s = Stack()
s.push("A")  # Sona ekler
s.push("B")
s.pop()  # Sondan siler pop(0) baştan siler.
print(s.get_stack())

