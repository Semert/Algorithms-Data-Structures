A1 = [1, 4, 9]

for i in reversed(range(len(A1))):
    # print(A1[i])
    print(i)

def deneme(a):
    a[-1] += 1
    for i in reversed(range(1,len(a))):
        if(a[i]) != 10:
            break
        a[i] = 0
        a[i-1] += 1

        if a[0] == 10:
            a[0] = 1
            a.append(0)

        return a

print(deneme(A1))