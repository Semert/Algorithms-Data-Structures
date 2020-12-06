def isLucky(n):
    strLucky = str(n)

    left, right = 0, len(strLucky) - 1

    sum1 = 0
    sum2 = 0

    while left < right:
        sum1 += int(strLucky[left])
        sum2 += int(strLucky[right])

        left += 1
        right -= 1

    return sum1 == sum2





