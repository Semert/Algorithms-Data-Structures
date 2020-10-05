# https://leetcode.com/problems/counting-bits/submissions/
class Solution(object):
    def countBits(self, num):
        arr = []

        # bin(2)[2:]

        for i in range(num + 1):
            arr.append(bin(i).count("1"))
        return arr

        # res = [0]
        # for i in range(1, num + 1):
        #     res.append(res[i // 2] + i % 2)
        # return res