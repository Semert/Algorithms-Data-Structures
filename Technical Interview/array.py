arr = [2,5,9,11,3,7]
arr2 = [2, 5, 1 , 9 , 11, 2]
arr3 =[5 , 9 , 11, 2]
arr4 = [3 , 12 , 5 , 9 , 1 , 11 , 2]

maximum = 0
enbuyuk = max(arr4)

# print(max)
# print(enbuyuk)
# arr.remove(11)
# arr.insert(0,11)
# print(arr)

m = max(arr4)
maxindex = ([i for i, j in enumerate(arr4) if j == m])
if(maxindex[0] == 0):
    arr4.pop(0)
    m = max(arr4)
    maxindex = ([i for i, j in enumerate(arr4) if j == m])


for i in range(maxindex[0]):
    if(m-arr4[i]>maximum):
        maximum= m-arr4[i]
print(maximum)

# for i in range(len(arr) - 1):
#     for j in range(i + 1, len(arr)):
#         if (arr[i] - arr[j] and arr[i]>arr[j]):
#             max = (arr[i] - arr[j])