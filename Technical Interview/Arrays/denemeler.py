n = 19
s="deneme"
print(list(s))
arr = [int(x) for x in str(n)]
print(arr)

def buy_and_sell(A):
    max_profit = 0


    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if A[j] - A[i] > max_profit:
                max_profit = A[j] - A[i]

    return  max_profit



def buy_and_sell2(prices):

    if len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price,price)
        compareprofit = price - min_price
        max_profit = max(max_profit,compareprofit)

    return  max_profit


def binary(data,target):
    low = 0
    high = len(data) -1

    while low <= high:
        mid = (low+high) // 2

        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
        return False