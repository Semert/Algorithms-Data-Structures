# https://leetcode.com/problems/power-of-two/submissions/
class Solution(object):
    def isPowerOfTwo(self, n):

        absoluteN = abs(n)

        if n == 1:
            return True

        count = 0
        while (absoluteN):
            absoluteN //= 2
            count += absoluteN

        return count + 1 == n

