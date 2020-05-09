
# https://www.hackerrank.com/challenges/kangaroo/problem
# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    # Best solution
    s1 = abs(x2-x1)
    s2 = abs(x2+v2-x1-v1)
    d = s1 - s2
    if d > 0:
        if s1%d == 0:
            return 'YES'
    return 'NO'

# Solution 2
i,count=1,False
    if v1<=v2 and x1<x2:
        return "NO"
    elif v1>v2 and x1>x2:
        return "NO"
    elif v1>v2 and x1<x2:
        while((x1+(i*v1))<=(x2+(i*v2))):
            if (x1+(i*v1))==(x2+(i*v2)):
                count=True
                break
            i+=1
        if count==True:
            return "YES"
        else:
            return "NO"
    else:
        return "YES"