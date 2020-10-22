# https://leetcode.com/problems/intersection-of-two-arrays/
class Solution(object):
    def intersection(self, nums1, nums2):
        num = []
        ht = {}

        for i in nums1:
            ht[i] = 1

        for i in nums2:
            if i in ht:
                ht[i] += 1

        for key, values in ht.items():
            if values > 1:
                num.append(key)

        return num