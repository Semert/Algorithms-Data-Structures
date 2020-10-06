# https://leetcode.com/problems/running-sum-of-1d-array/submissions/
class Solution(object):
    def runningSum(self, nums):
        arr = [0] * len(nums)

        arr[0] = nums[0]

        for i in range(1, len(nums)):
            arr[i] = arr[i - 1] + nums[i]

        return arr