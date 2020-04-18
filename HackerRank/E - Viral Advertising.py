# https://www.hackerrank.com/challenges/strange-advertising/problem
import math
def viralAdvertising(n):
    shared = 5
    cumulative = 0
    for i in range(n):
        liked = math.floor(shared/2)
        shared = liked *3
        cumulative += liked
    return cumulative
