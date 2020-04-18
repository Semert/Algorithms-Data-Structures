def extraLongFactorials(n):
    fact = 1
    for i in range(n,0,-1):
        fact *= i
    print(fact)
