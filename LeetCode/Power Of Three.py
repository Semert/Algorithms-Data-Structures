# https://leetcode.com/problems/power-of-three/submissions/
class Solution(object):
    def isPowerOfThree(self, n):

        # Faster

        # if n < 1:
        #     return False
        #
        # while (n % 3 == 0):
        #     n //= 3
        #
        # return n == 1

        absoluteN = abs(n)

        if n == 1:
            return True

        count = 0
        while (absoluteN):
            absoluteN //= 3
            count += absoluteN

        return (count * 2) + 1 == n
