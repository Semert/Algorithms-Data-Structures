
# https://www.hackerrank.com/challenges/kangaroo/problem
# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    # Best solution
    s1 = abs(x2-x1)
    s2 = abs(x2+v2-x1-v1)
    d = s1 - s2
    if d > 0:
        if s1%d == 0:
            return 'YES'
    return 'NO