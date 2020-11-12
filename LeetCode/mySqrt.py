# https://leetcode.com/problems/sqrtx/submissions/

class Solution(object):
    def mySqrt(self, x):

        left, right = 0, x

        while left <= right:

            mid = (right + left) // 2
            square = mid ** 2

            if square <= x:
                left = mid + 1

            elif square > x:
                right = mid - 1

        return left - 1