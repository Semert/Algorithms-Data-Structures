# https://leetcode.com/problems/length-of-last-word/submissions/

class Solution(object):
    def lengthOfLastWord(self, s):

        length = 0
        s = s.strip()

        for i in range(len(s) - 1, -1, -1):

            if (s[i] == " "):
                return length

            length += 1

        return length