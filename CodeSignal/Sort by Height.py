# https://app.codesignal.com/arcade/intro/level-3/D6qmdBL2NYz49XHwM
def sortByHeight(a):
    arr = []
    result = []
    c = 0
    for index, item in enumerate(a):
        print(index, item)
        if item != -1:
            arr.append(item)

    arr.sort()

    for i in a:
        if i == -1:
            result.append(-1)
        else:
            result.append(arr[c])
            c += 1

    return result