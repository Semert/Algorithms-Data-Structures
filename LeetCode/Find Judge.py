# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3325/

class Solution(object):
    def findJudge(self, N, trust):
        if (N == 1):
            return 1
        if (len(trust) == 0):
            return -1

        trustCount = [0 for x in range(len(trust) + 1)]
        for i in trust:
            trustCount[i[1] - 1] += 1
            trustCount[i[0] - 1] -= 1

        for i in range(N):
            if (trustCount[i] == N - 1):
                return i + 1

        return -1