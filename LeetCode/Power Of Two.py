# https://leetcode.com/problems/power-of-two/submissions/
class Solution(object):
    def isPowerOfTwo(self, n):

        a = abs(n)

        if n == 1:
            return True

        count = 0
        while (a):
            a //= 2
            count += a

        if (count + 1 == n):
            return True
        else:
            print(count + 1)

            return False
