
# https://www.hackerrank.com/challenges/apple-and-orange/problem
def countApplesAndOranges(s, t, a, b, apples, oranges):
    count1=0
    count2=0
    for x in apples:
        if x+a>=s and x+a<=t:
            count1+=1
    for y in oranges:
        if y+b<=t and y+b>=s:
            count2+=1
    print(count1,count2,sep='\n')

https://www.competitive-programming.com/2020/04/calculate-running-time-of-algorithm.html