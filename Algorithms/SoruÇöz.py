import math
# x = math.ceil(9/2)
# y = math.ceil(-23/2)
# print(y)
# #
# t = bin(5)
# print(x)
# print(t)
# n = "101"
#
# def binaryToDecimal(n):
#     return int(n,2)
# print(binaryToDecimal(n))

# a = [1, 0, 0, 1, 1]
# a =[1, 0, 0, 1, 1, 1]
# a = ''.join(map(str, a))
# print(a)
# # print(n)
# # print(binaryToDecimal(a))
# # print(binaryToDecimal(n))
# deneme = int("100111",2)
# print(deneme)

a = [1, 0, 0, 1, 1]
a = [1,0,0,1,1,1]
# a = [1,0,1,1]
# a = [1,0,1,0,1,1]
newarr = []

for i in range(len(a)):
    if(i%2==1):
        newarr.append(a[i]*-2**i)
    else:
        newarr.append(a[i]*2**i)
print(sum(newarr))


yeni = sum(newarr)
# print(yeni)
x = math.ceil((yeni)/2)
print(x)
print("---------")
sayı = 11
print("sayı",sayı)
at = sayı%2
sayı = sayı//2
print(at)

print("sayı",sayı)

at = sayı%2
sayı = sayı//2
print("sayı",sayı)


print(at)

at = sayı%2
sayı = sayı//2

print(at)
print("son")
print("sayı",sayı)
array = [ 1,  -2,  4,  -8,  16,  -32]

# print(sayı)

# t = bin(2**3)
# print(t)
# if(yeni<0):
#     o = t[3:]
# else:
#     o = t[2:]
# print(o)
#
# print([int(y) for y in o])

# print(type(t))

newarr = []

for i in range(len(a)):
    if (i % 2 == 1):
        newarr.append(a[i] * -2 ** i)
    else:
        newarr.append(a[i] * 2 ** i)
    print(sum(newarr))
    yeni = sum(newarr)
    x = math.ceil((yeni) / 2)
    t = bin(x)
    if (yeni < 0):
        o = t[3:]
    else:
        o = t[2:]
    print(o)

    print([int(y) for y in o])