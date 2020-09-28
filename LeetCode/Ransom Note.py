# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3318/
class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        if len(ransomNote) > len(magazine):
            return False

        ht = {}
        for x in magazine:
            if x in ht:
                ht[x] += 1
            else:
                ht[x] = 1

        for char in ransomNote:
            if char not in ht:
                return False
            if ht[char] <= 0:
                return False
            ht[char] -= 1
        return True

