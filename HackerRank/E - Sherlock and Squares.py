# https://www.hackerrank.com/challenges/sherlock-and-squares/problem
import math

def squares(a, b):
    count=0
    c=int(math.sqrt(b))
    for i in range(1,c+1):
        if i**2 in range(a,b+1):
            count+=1
    return count