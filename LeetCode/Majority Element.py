# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3321/
class Solution(object):
    def majorityElement(self, nums):

        ht = {}
        for x in nums:
            if x in ht:
                ht[x] += 1
            else:
                ht[x] = 1

        for key, value in ht.items():
            if value == max(ht.values()):
                return key

