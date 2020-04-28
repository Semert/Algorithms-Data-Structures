# https: // www.hackerrank.com / challenges / equality - in -a - array / problem


def equalizeArray(arr):
    ht = dict()
    count = 0
    for a in arr:
        if a in ht:
            ht[a] += 1
        else:
            ht[a] = 1
    maxocc = max(ht.values())
    for k, v in ht.items():
        if (v < maxocc):
            count += arr.count(k)
    return count

    max_c = -1
    max_item = None
    count = {}
    for item in aRR:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
        if count[item] > max_c:
            max_c = count[item]
            max_item = item

    return (len(aRR) - max_c)


def equalizeArray(arr):
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return len(arr) - max(d.values())