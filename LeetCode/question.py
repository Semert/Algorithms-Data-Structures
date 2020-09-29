
num = 35
c = "2"

# arr = [str(x) for x in num]

def countNum(num,c):
    arr = [x for x in range(num+1)]
    full_str = ''.join([str(x) for x in arr])
    print(full_str.count(c))




countNum(num,c)