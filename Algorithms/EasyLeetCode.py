# https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        l = 0
        r = 0
        for i in s:
            if i == 'L':
                l += 1
            if i == 'R':
                r += 1
            if(r!=0 and l!=0 and r==l):
                result += 1
                r=0
                l=0
        return result

#------------------------------------------------------------------

# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# https://leetcode.com/problems/defanging-an-ip-address/
class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        while (num != 0):
            count += 1
            if num % 2 == 0:
                num = num / 2
            elif num % 2 == 1:
                num -= 1

        return count
#------------------------------------------------------------------
