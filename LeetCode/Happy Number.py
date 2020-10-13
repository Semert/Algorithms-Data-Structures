# https://leetcode.com/problems/happy-number/submissions/
class Solution(object):
    def isHappy(self, n):
        # arr = [int(x) for x in str(n)]
        #
        # toplama = 0
        # count = 0
        # while toplama != 1:
        #     for i in arr:
        #         toplama += i ** 2
        #     count += 1
        #
        #     arr = [int(x) for x in str(toplama)]
        #     if (toplama <= 1):
        #         return True
        #     toplama = 0
        #     if (count > 5):
        #         return False

        def karenumber(num):
            result = 0
            while (num>0):
                first = num % 10
                result += first * first
                num //= 10
            return result

        Seen = set()

        while karenumber(n) not in Seen:
            total = karenumber(n)
            if (total == 1):
                return True
            else:
                Seen.add(total)
                n = total
        return False

