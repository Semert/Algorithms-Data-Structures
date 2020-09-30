# https://leetcode.com/problems/missing-number/submissions/
class Solution(object):
    def missingNumber(self, nums):
        total = 0
        n = len(nums)

        for i in range(len(nums)):
            total += nums[i]

        return (n * (n + 1)) / 2 - total

