# https://leetcode.com/problems/detect-capital/submissions/
class Solution(object):
    def detectCapitalUse(self, word):

        count = 0

        for char in word:

            if char.isupper():
                count += 1

        return count == len(word) or count == 0 ount == 1 and word[0].isupper())r (co