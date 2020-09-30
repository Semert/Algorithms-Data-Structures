class Solution(object):
    def isPowerOfThree(self, n):

        absoluteN = abs(n)

        if n == 1:
            return True

        count = 0
        while (absoluteN):
            absoluteN //= 3
            count += absoluteN

        return (count * 2) + 1 == n
