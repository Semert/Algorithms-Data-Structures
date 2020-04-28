# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i=0
    hops = 0
    while i<n-2:
        #print(c[i+2])
        if c[i+2]==0:
            hops +=1
            i+=2
            #print('hopped 2 steps')
        else:
            hops +=1
            i+=1
            #print('hopped 1 step')
    #print(hops)
    print(n)
    if i+2 ==n:
        print(n)
        hops +=1
    return hops