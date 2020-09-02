# ar = [3, 2, 1, 3]

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
# ------------------------------------------------------
# python slice
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x])
# ------------------------------------------------------

# python enumerate
x = ('apple', 'banana', 'cherry')
y = enumerate(x)

print(list(y))

y = enumerate(x, 10)
print(list(y))

# ------------------------------------------------------


grocery = ['bread', 'milk', 'butter']

print('\n')
for item in enumerate(grocery):
  print(item)

print('\n')
for count, item in enumerate(grocery):
  print(item)

print('\n')
for count, item in enumerate(grocery):
  print(count, item)

print('\n')
# changing default start value
for count, item in enumerate(grocery, 100):
  print(count, item)

# ------------------------------------------------------
# python split

text = 'geeks for geeks'

# Splits at space
print(text.split())

word = 'geeks, for, geeks'

# Splits at ','
print(word.split(', '))

word = 'geeks:for:geeks'

# Splitting at ':'
print(word.split(':'))

# ------------------------------------------------------



word = 'CatBatSatFatOr'

# Splitting at 3
print([word[i:i + 3] for i in range(0, len(word), 3)])

# ------------------------------------------------------


word = 'geeks, for, geeks, pawan'

# maxsplit: 0
print(word.split(', ', 0))

# maxsplit: 4
print(word.split(', ', 4))

# maxsplit: 1
print(word.split(', ', 1))

# ------------------------------------------------------
