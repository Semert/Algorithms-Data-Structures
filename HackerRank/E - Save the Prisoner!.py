n = 7
m = 19
s=2

haha = [a for a in range(1,n+1)]
print(haha)
s = s-1
m = m-1

arr = (haha[s:]+haha[:s])
print(arr)
print(m)
while True:
    # if (m >= len(arr)):
    #     m = m - len(arr)
    # if(m<len(arr)):
    #     break
    if (m >= n):
        m = m%n
    if (m < len(arr)):
        break
print(m)



print(arr[m])


def saveThePrisoner(n, m, s):
    candyChair = ((s-1)+m)%n;

    if(candyChair==0):
        return n;
    else:
        return candyChair;

def saveThePrisoner(n, m, s):
    if(((m+s-1)%n)==0):
        return n
    else:
        return ((m+s-1)%n)