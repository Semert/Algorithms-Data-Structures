list1 = [11,3,2,55,7,0]
print("Unsorted list ", list1)

for i in range(len(list1)):
    min_value = min(list1[i:]) # Her aşamada i kadar element atlayacak.
    min_index = list1.index(min_value)
    list1[i],list1[min_index] = list1[min_index],list1[i]

print("Sorted list ", list1)

print("--------------------------------------")
# Works For Duplicate values
list1 = [11,0,3,2,2,55,7,0]
print("Unsorted list ", list1)

for i in range(len(list1)):  # -1 yaparsak son elemen zaten sort olmuş olacağı için bir sorun olmaz.

    min_value = min(list1[i:]) # Her aşamada i kadar element atlayacak.
    min_index = list1.index(min_value,i)
    list1[i],list1[min_index] = list1[min_index],list1[i]
print("Sorted List", list1)

for i in range(len(list1)-1):  # -1 yaparsak son elemen zaten sort olmuş olacağı için bir sorun olmaz.

    min_value = min(list1[i:]) # Her aşamada i kadar element atlayacak.
    min_index = list1.index(min_value,i)
    if list1[i] != list1[min_index]: #Aynı sayıları swap etmesine gerek yok.
        list1[i],list1[min_index] = list1[min_index],list1[i]
print("Sorted List", list1)



print("--------------------------------------")




