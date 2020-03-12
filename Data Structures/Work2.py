def staircase(n):
    for i in range(1, n + 1):
        print(str('#' * i).rjust(n))


staircase(6)

# a = n
# count = 0
# for i in range(a, 0, -1):
#     print(" " * i, end='')
#     count += 1
#     print('#' * count)