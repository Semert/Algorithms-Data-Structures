# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3316/
class Solution(object):
    def firstBadVersion(self, n):

        right = n
        left = 1
        middle = 0

        while (left < right):
            middle = (right + left) // 2

            if (isBadVersion(middle)):
                right = middle
            else:
                left = middle + 1

        return left


