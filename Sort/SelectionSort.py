list1 = [11,3,2,55,7,0]
print(list1)

for i in range(len(list1)):
    min_value = min(list1[i:]) # Her aşamada i kadar element atlayacak.
    min_index = list1.index(min_value)
    list1[i],list1[min_index] = list1[min_index],list1[i]
    
print(list1)