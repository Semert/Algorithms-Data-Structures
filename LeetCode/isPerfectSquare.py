class Solution(object):
    def isPerfectSquare(self, num):

        left = 0
        right = num
        middle = 0
        if (num == 1):
            return True

        while (left <= right):
            middle = (right + left) // 2

            if (middle * middle == num):
                return True
            elif (middle * middle < num):
                left = middle + 1
            else:
                right = middle - 1

        return False
