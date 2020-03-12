data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 25

# Linear Search
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
        return False

# Iterative Binary Search
def binary_search_iterative(arr,target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == arr[mid]
            return True
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
        return False