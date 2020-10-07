# https://leetcode.com/problems/monotonic-array/submissions/


class Solution(object):
    def isMonotonic(self, A):

        i, j = 0, 0

        print(len(A))

        while i <= len(A) - 2 and j <= len(A) - 2:

            if (A[i] > A[i + 1] or A[i] == A[i + 1]):
                i += 1
            else:
                while j <= len(A) - 2:
                    if (A[j] < A[j + 1] or A[j] == A[j + 1]):
                        j += 1
                    else:
                        return False

        if (i == len(A) - 1 or j == len(A) - 1):
            return True
        else:
            return False

#         inc = True
#         dec = True

#         for i in range(len(A)-1):

#             if A[i] > A[i+1]:

#                 dec = False

#             if A[i] < A[i+1]:

#                 inc = False

#         return inc or dec
