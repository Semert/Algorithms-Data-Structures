"""
Stack Data Structure.
"""

#
# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def is_empty(self):
#         return self.items == []  # True or False
#
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]  # Sondaki elemanı verir.
#
#     def get_stack(self):
#         return self.items
#
#
# s = Stack()
# s.push("A")  # Sona ekler
# s.push("B")
# s.pop()  # Sondan siler pop(0) baştan siler.
# print(s.get_stack())

#-------------------------
arr = [1,2,3,4,5]
#arr = [7,69,2,221,8974]

arr.sort()

new_arr = arr[::-1]
sum1 = []
sum2 = []
for array in arr:
    sum1.append(array)
for i in new_arr:
    sum2.append(i)
print(sum1)
z = sum(sum1)
c = sum(sum2)
x = z - arr[-1]
y = c - new_arr[-1]

print(x,y)
#--------------------------------