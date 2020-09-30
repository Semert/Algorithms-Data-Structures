# https://leetcode.com/problems/valid-palindrome/submissions/
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # s = [i for i in s if i.isalnum()]
        # s = ''.join(s).lower()
        # return s == s[::-1]

        actual_str = "".join(x for x in s if x.isalnum()).lower()

        def checkPalindrome(s):
            i = 0
            j = len(s) - 1

            while (i < j):
                if (s[i] == s[j]):
                    j -= 1
                    i += 1
                else:
                    return False
            return True

        return checkPalindrome(actual_str)
