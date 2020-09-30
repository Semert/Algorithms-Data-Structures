# https://leetcode.com/problems/excel-sheet-column-number/submissions/
class Solution(object):
    def titleToNumber(self, s):
        value = 0
        n = len(s) - 1

        for i in range(len(s)):
            value += (26 ** n) * (ord(s[i]) - 64)
            n -= 1

        return value
