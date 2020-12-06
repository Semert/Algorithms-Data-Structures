def trailingZeroes(n):
    # Fast
    count = 0
    while n:
        n //= 5
        count += n
    return (count)
    # BruteForce
    # fact = 1
    # for i in range(n, 0, -1):
    #     fact *= i
    # count = 0
    # stfact = str(fact)
    # for i in range(len(stfact)-1,-1,-1):
    #     if(stfact[i] == "0"):
    #         count += 1
    #     else:
    #         break
    # return count




print(trailingZeroes(10))
arr = [x for x in range(4) if x % 2 == 0]
s = "deneme"
print(arr)
print("".join([str(x) for x in arr]))
print("".join(map(str,arr)))
print(s.count("e"))
arr2 = [0,1,2,3]
print(arr2[:-1])

arr3 = [1,2,3]
arr4 = [0] * len(arr3)
print(max(-12,-15))
print(arr4)