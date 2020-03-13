# Some easy Questions.

#-----------------------------------------
# Mini-Max Sum
arr = [7,69,2,221,8974]

def miniMaxSum(arr):
    arr.sort()
    array = arr.copy()
    a = []
    b = []

    def funcMax():
        max = 0
        for i in range(len(arr)):
            if ( arr[i] > max):
                max = arr[i]
        return max

    def funcMin():
        min = arr[-1]
        for i in range(len(array)):
            if ( array[i] < min):
                min = array[i]
        return min
    for i in range(1,len(array)):
        array.remove(funcMin())
        b.append(funcMin())

    for i in range(1,len(arr)):
        arr.remove(funcMax())
        a.append(funcMax())
    print(sum(a),sum(b))
#-----------------------------------------
