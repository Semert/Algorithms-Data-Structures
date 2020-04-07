# Happy number LeetCode
# n=19
# def isHappy(n):
#     arr = [int(x) for x in str(n)]
#     toplama = 0
#     count = 0
#     while toplama != 1:
#         for i in arr:
#             toplama += i ** 2
#         count += 1
#         arr = [int(x) for x in str(toplama)]
#         if(toplama <= 1):
#             return True
#         toplama = 0
#         if(count>15):
#             return False
#
#
# print(isHappy(n)),

#--------------------------------
# Move Zeros
# nums = [1,2,0,3,0,4]
# a.remove(0)
# print(a)

#
# for i in nums:
#     if i==0:
#         nums.remove(i)
#         nums.append(0)
# print(nums)

# j = 0  # position of 1st 0
#
# for i in range(len(nums)):
#     if nums[i] != 0:
#         print(nums,i,j)
#         print(nums[i],nums[j])
#         nums[i], nums[j] = nums[j], nums[i]
#         j += 1
#
# print(nums)

#--------------------------------
# Maximum SubArray
def maxSubArray(nums):
    # we are taking two varible total_sum and max_sum
    # total_sum will take care of sum till every index and max_sum will the max(total_sum, max_sum)
    total_sum = max_sum = nums[0]
    # in starting we are giving value to both total_sum and max_sum as value at index 0
    for i in nums[1:]:  # looping the array starting from index 1

        total_sum = max(i, total_sum + i)  # computing total sum
        max_sum = max(total_sum, max_sum)  # updating max_sum if total_sum is larger than max_sum

    return max_sum