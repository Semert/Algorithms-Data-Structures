arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]

def sockMerchant(n, ar):
    ht = dict()
    for i in ar:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    count = 0
    for k,v in ht.items():
        count += v//2
    return count