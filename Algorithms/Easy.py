import math
import os
import random
import re
import sys
#---------------------------------------
# StairCase

# Write a program that prints a staircase of size n
# def staircase(n):
#     for i in range(1, n + 1):
#         print(str('#' * i).rjust(n))
#
#
# staircase(6)

     #
    ##
   ###
  ####
 #####
######

# The other way to solve, not working in HackerRank.
# a = n
# count = 0
# for i in range(a, 0, -1):
#     print(" " * i, end='')
#     count += 1
#     print('#' * count)
#---------------------------------------

#---------------------------------------
# Diagonal Difference

# def diagonalDifference(arr):
#     # Write your code here
#     count = -1
#     x = 0
#     y = 0
#     for a in range(len(arr)):
#         x += arr[a][a]
#         y += arr[a][count]
#         count += -1
#     return abs(x - y)
#
#---------------------------------------

#---------------------------------------
# Plus Minus

# Complete the plusMinus function below.
# def plusMinus(arr):
#     length = len(arr)
#     x=0
#     y=0
#     z=0
#     for a in arr:
#         if(a<0):
#             x+=1
#         elif(a>0):
#             y+=1
#         else:
#             z+=1
#     o = y/length
#     t = x/length
#     l = z/length
#     print("%.6f" % o)
#     print("%.6f" % t)
#     print("%.6f" % l)
    #print(y/length,x/length,z/length)
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
# def breakingRecords(scores):
#     first = scores[0]
#     low = scores[0]
#     count = 0
#     count2 = 0
#     for i in range(1, len(scores)):
#         if (first < scores[i]):
#             first = scores[i]
#             count += 1
#         if (low > scores[i]):
#             low = scores[i]
#             count2 += 1
#     return count, count2
#---------------------------------------
# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

# def breakingRecords(scores):
#     first = scores[0]
#     low = scores[0]
#     count = 0
#     count2 = 0
#     for i in range(1, len(scores)):
#         if (first < scores[i]):
#             first = scores[i]
#             count += 1
#         if (low > scores[i]):
#             low = scores[i]
#             count2 += 1
#     return count, count2
#
#
#---------------------------------------
# https://www.hackerrank.com/challenges/bon-appetit/problem
def bonAppetit(bill, k, b):
    sumarr = 0
    for i in range(len(bill)):
        if (i == k):
            continue
        sumarr += bill[i]
    sumarr = sumarr // 2
    sumarr = abs(sumarr - b)

    if (sumarr == 0):
        print('Bon Appetit')
    else:
        print(sumarr)
