def findDigits(n):
    count=0
    for i in str(n):
        if (int(i)!=0 and n%int(i)==0):
            count += 1
    return count


def findDigits2(n):
    a=[int(x) for x in str(n)]
    count=0
    for a in a:
        if (a != 0 and n%a == 0):
            count += 1
    return count

# 2 answer added.