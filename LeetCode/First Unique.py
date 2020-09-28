# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3320/
class Solution(object):
    def firstUniqChar(self, s):

        dict = {}
        idx = 0
        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        print(dict)

        for char in s:
            if (dict[char] == 1):
                return s.index(char)

        if (s == "" or s):
            return -1