# https://leetcode.com/problems/roman-to-integer/submissions/
class Solution(object):
    def romanToInt(self, s):
        res = 0
        hashmap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for i, x in enumerate(s[:-1]):
            if hashmap[x] < hashmap[s[i + 1]]:
                res -= hashmap[x]
            else:
                res += hashmap[x]

        return res + hashmap[s[-1]]