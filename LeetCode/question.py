
num = 35
c = "2"


def countNum(num,c):
    arr = [x for x in range(num+1)]
    full_str = ''.join([str(x) for x in arr])
    print(full_str.count(c))




countNum(num,c)
countNum(30,"1")
countNum(50,"7")
# num ve c değerlerini değiştirip test edebilirsiniz. [num -> int, c -> str]