ar = [3, 2, 1, 3]

# a= 67
# b = a%5
# # a = a - b
# print(a/5)
# d = a/5+1
# print(d*5)
# print(a)
# print()
# print(d*5-a)
#
# lst = [73, 67, 38, 33]
# lst2 = [37, 38]
# def gradingStudents(grades):
#     grades1 = []
#     gradeler = []
#     for a in grades:
#         b = a%5
#         c = a-b
#         beslikler = c + 5
#
#         if(beslikler-a<3 and beslikler>38):
#             grades1.append(int(beslikler))
#         else:
#            grades1.append(a)


#     print(grades1)
# print(gradingStudents(lst))

# python slice
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x])

# python enumerate
x = ('apple', 'banana', 'cherry')
y = enumerate(x)

print(list(y))

y = enumerate(x, 10)
print(list(y))