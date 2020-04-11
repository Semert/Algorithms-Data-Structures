A1 = [1, 4, 9]
A2 = [9, 9, 9]

# s = ''.join(map(str, A))
# print(int(s) + 1)


def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):  # For işlemini tersten yapar
        if A[i] != 10:
            break
        A[i] = 0  # son elemanı 0 yap
        A[i-1] += 1  # sondan bir önceki elemanı 1 arttır.
    if A[0] == 10:  # Eğer ilk eleman 10'a eşit ise ilk elemanı '1' yap sona '0' ekle.
        A[0] = 1
        A.append(0)
    return A


print(plus_one(A1))
print(plus_one(A2))