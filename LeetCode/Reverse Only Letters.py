# https://leetcode.com/problems/reverse-only-letters/submissions/
class Solution(object):
    def reverseOnlyLetters(self, S):
        # turn string into a list for easy manipulation.
        S = list(S)
        # pointers to keep track of letters.
        i, j = 0, len(S) - 1
        # go through string and reverse letters only.
        while i < j:
            if S[i].isalpha() and S[j].isalpha():
                temp = S[i]
                S[i] = S[j]
                S[j] = temp
                i += 1
                j -= 1
            if not S[i].isalpha():
                i += 1
            if not S[j].isalpha():
                j -= 1
        # return reversed string.
        return "".join(S)