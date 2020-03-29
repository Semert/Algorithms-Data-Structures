list1 = [11,3,2,55,7,0]
print("Unsorted list ", list1)

for i in range(len(list1)):
    min_value = min(list1[i:]) # Her aşamada i kadar element atlayacak.
    min_index = list1.index(min_value)
    list1[i], list1[min_index] = list1[min_index], list1[i]

print("Sorted list ", list1)

print("--------------------------------------")

# Works For Duplicate values
list1 = [11,0,3,2,2,55,7,0]
print("Unsorted list ", list1)

for i in range(len(list1)):  # -1 yaparsak son elemen zaten sort olmuş olacağı için bir sorun olmaz.
    min_value = min(list1[i:]) # Her aşamada i kadar element atlayacak.
    min_index = list1.index(min_value,i)
    list1[i], list1[min_index] = list1[min_index], list1[i]

print("Sorted List", list1)

for i in range(len(list1)-1):  # -1 yaparsak son elemen zaten sort olmuş olacağı için bir sorun olmaz.
    min_value = min(list1[i:]) # Her aşamada i kadar element atlayacak.
    min_index = list1.index(min_value,i)
    if list1[i] != list1[min_index]: #Aynı sayıları swap etmesine gerek yok.
        list1[i], list1[min_index] = list1[min_index], list1[i]

print("Sorted List", list1)

print("--------------------------------------")

# Without using built method (min)
list1 = [11,3,2,55,7,0]
print("Unsorted list ", list1)

for i in range(len(list1)-1):
    min_value = list1[i]
    for j in range(i+1,len(list1)):
        if list1[j] < min_value:
            min_value = list1[j]
    min_index = list1.index(min_value)
    if list1[i] != list1[min_index]:
        list1[i], list1[min_index] = list1[min_index], list1[i]
print("Sorted List", list1)

# Duplicate values

list1 = [11,0,3,2,2,55,7,0]
print("Unsorted list ", list1)

for i in range(len(list1)-1):
    min_value = list1[i]
    for j in range(i+1,len(list1)):
        if list1[j] < min_value:
            min_value = list1[j]

    min_index = list1.index(min_value,i)
    if list1[i] != list1[min_index]:
        list1[i], list1[min_index] = list1[min_index], list1[i]
print("Sorted List", list1)

print("--------------------------------------")


# Büyükten Küçüğe [Descending order]

list1 = [11,0,3,2,2,55,7,0]
print("Unsorted list ", list1)

for i in range(len(list1)-1):
    max_value = list1[i]
    for j in range(i+1,len(list1)):
        if list1[j] > max_value:
            max_value = list1[j]

    max_index = list1.index(max_value,i)
    if list1[i] != list1[max_index]:
        list1[i], list1[max_index] = list1[max_index], list1[i]
print("Sorted List", list1)

print("--------------------------------------")

# Without using index method

# list1 = [11,0,3,2,2,55,7,0]
# print("Unsorted list ", list1)
#
# for i in range(len(list1)-1):
#     max_index = i
#     for j in range(i+1,len(list1)):
#         if list1[j] < list1[max_index]:
#             max_index = j
#
#     if list1[i] != list1[max_index]:
#         list1[i], list1[max_index] = list1[max_index], list1[i]
# print("Sorted List", list1)


# num = int(input("how many numbers you want to enter?"))
# list2 = [int(input("Enter number")) for x in range(num)]



