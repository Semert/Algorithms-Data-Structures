# https://leetcode.com/problems/uncommon-words-from-two-sentences/submissions/
class Solution(object):
    def uncommonFromSentences(self, A, B):

        A = A.split(" ")
        B = B.split(" ")

        ht = {}
        arr = []

        for i in A:
            if i in ht:
                ht[i] += 1
            else:
                ht[i] = 1

        for i in B:
            if i in ht:
                ht[i] += 1
            else:
                ht[i] = 1

        for key, value in ht.items():
            if (value < 2):
                arr.append(key)

        return arr