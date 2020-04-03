"""
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

Example:
nums = [1, 3, 11, 2, 7]
target = 9
return : [3,4]
9 - 1 = 8 -> {8 : 0}
9 - 3 = 6 -> {8 : 0, 6 : 1}
9 - 11 = -2 -> {8 : 0, 6 : 1, -2 : 2}
9 - 2 = 7 -> {8 : 0, 6 : 1, -2 : 2, 7 : 3}

nums[i], i
"""

nums = [1, 3, 11, 2, 7]
target = 9


def two_sum(nums, target):
    if len(nums) <= 1:
        return False

    aux_dict = {}
    for i in range(len(nums)):
        if nums[i] in aux_dict:
            return [aux_dict[nums[i]], i]
        else:
            aux_dict[target - nums[i]] = i


def binary_search_solution(nums,target):

    if len(nums) <= 1:
        return False

    low = 0
    high = len(nums)-1
    value = 0

    while(low < high):
        value = nums[low] + nums[high]
        if(target == value):
            return True
        if(value < target):
            low += 1
        if(value > target):
            high -= 1
    return False


def twoSum(nums, target):

    numbersSeen = {}

    for (index, number) in enumerate(nums):

        difference = target-number

        if difference in numbersSeen:
            return (index, numbersSeen[difference])

        numbersSeen[number] = index

    return ()



print(two_sum(nums, target))
