
# l1=[]
# for x in range(1,11):
#     l1.append(x**2)
#
# print(l1)
# print(x) # x değişkeni istemediğimiz halde var. Lambda kullanınca sadece çalışırken var oluyor sonra yok oluyor.
# print("----------------------")
#
# def abc(x):
#     return x+5
# l2 = [1,2,3]
# print(list(map(abc,l2)))
# # Bu işlemde x, çalıştıktan sonra yok olur.
# print(list(map(lambda x: x+5, range(1,11))))
# print(list(map(lambda x: x**2, range(1,11))))
# print("----------------------")
# squares = [x**2 for x in range(1,11)]
# squares2 = [x**2 for x in range(1,11) if(x%2==0)] # x**2 1'den 10'a 2'ye bölünebilenleri yazdır.
# print(squares)
# print(squares2)
# print(x) # x'i yine yazdı ama bu işlem daha pratik. one line.

print("----------------------")
l3 = [(x,x**2) for x in range(2,4)]
print(l3)

for x,y in l3:
    print(x,y)
liste = [(x,y) for x in [1,2,3] for y in [3,1,4] if(x==y)]

liste2 = [(x,y) for x in [1,2,3] for y in [3,1,4] if(x!=y)]

liste3 = [(x,y,z) for x in [1,2,3] for y,z in [(3,1),(1,2),(4,3)] if(x!=y)]
print(liste)
print(liste2)
print(liste3)
print("----------------------")

l5 = [1,2,3,1,2]
k = set(l5)     #Küme tekrarları yazmaz. String içinde geçerli.
print(l5)
print(k)

print("----------------------")

deneme = {"no":123, "no 2":345}
print(deneme["no"])
for key, value in deneme.items():
    print(key,value)

k2 = {x: x**2 for x in range(1,5)}
print(k2)
print("----------------------")
#
# def scopetest():
#     def do_local():
#         spam = "local spam"
#
#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"
#
#     def do_global():
#         global spam
#         spam = "global spam"
#
#     spam = "test spam"
#
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)
#
# scopetest()
# print("In global Scope", spam)
# #local cağrılamaz, nonlocalde çağrılamaz ama önceki spam değerini değiştirir.
# #Global olan heryerden çağrılabilir.
# print("----------------------")
#
# class araba():
#     hiz = 0
#     renk = ""
#     def hizlan(self):
#         self.hiz += self.hiz
#
# x = araba()
# x.hiz = 100
# x.hizlan()
#
# y = araba()
# y.hiz = 70
# y.hizlan()
#
# print("x arabanın hızı " , x.hiz)
# print("y arabanın hızı " , y.hiz)

# #############
# def topla(x,y):
#     return x+y
# print(topla(3,5))
# #######
# sum = lambda x,y : x+y
# print(sum(3,5))
# #######
# mx = lambda x,y: x if x > y else y
# print(mx(3,5))
# #############

# #############
# lst1=[1,2,3,4]
# def square(lst1):
#     lst2 = []
#     for num in lst1:
#         lst2.append(num ** 2)
#     return lst2
#
# print(square(lst1))
#
# print(list(map(lambda x:x**2,lst1)))
#
# print(list(filter(lambda x:x>2,lst1)))
#
# # List compherension
# print([x**2 for x in lst1])
# print([x for x in lst1 if x>2])
# #############
#
