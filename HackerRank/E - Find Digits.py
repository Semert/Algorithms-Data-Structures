# def findDigits(n):
#     count=0
#     for i in str(n):
#         if (int(i)!=0 and n%int(i)==0):
#             count += 1
#     return count
#
# # Solution 2
# def findDigits2(n):
#     a=[int(x) for x in str(n)]
#     count=0
#     for a in a:
#         if (a != 0 and n%a == 0):
#             count += 1
#     return count

arr =  [1,2,3]

ht = {}

for i in range(len(arr)):
    if arr[i] in ht:
        ht[i] += 1
    else:
        ht[i] = 1
    print(i)