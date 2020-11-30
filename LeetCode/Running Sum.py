# https://leetcode.com/problems/running-sum-of-1d-array/submissions/

def runningSum(nums):




    arr = [0] * len(nums)

    arr[0] = nums[0]

    for i in range(1, len(nums)):
        print(arr)
        arr[i] = arr[i - 1] + nums[i]

    return arr

print(runningSum([1,2,3,4,5]))