# https://leetcode.com/problems/guess-number-higher-or-lower/submissions/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        left = 0
        right = n

        while (left <= right):
            mid = (left + right) // 2
            myguess = guess(mid)
            if myguess == 0:
                return mid
            elif myguess == -1:
                right = mid - 1
            elif myguess == 1:
                left = mid + 1