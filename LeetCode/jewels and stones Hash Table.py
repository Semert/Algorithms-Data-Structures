# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/

class Solution(object):
    def numJewelsInStones(self, J, S):
        count = 0

        ht = {}

        for i in S:
            if i in ht:
                ht[i] += 1
            else:
                ht[i] = 1

        for key, value in ht.items():
            if key in J:
                count += 1 * value

        return count



