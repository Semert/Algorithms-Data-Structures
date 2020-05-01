# https://www.hackerrank.com/challenges/mini-max-sum/problem
def miniMaxSum(arr):
    arr = sorted(arr)
    print(sum(arr[:-1]),sum(arr[1:])

#Solution 2
s = sum(arr)
minmax = []
for i in arr:
    minmax.append(s-i)
print(min(minmax), max(minmax))
# Solution 3
l=[]
for i in range(len(arr)):
		l.append(sum(arr)-arr[i])
print(min(l),max(l))