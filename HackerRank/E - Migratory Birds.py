arr = [1,1,4, 4, 4,3,3, 3,5]

def migratoryBirds(arr):
    ht = dict()
    for i in arr:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    result = []
    for k,v in ht.items():
        if ( ht[k] == max(ht.values())):
            result.append(k)
    return(min(result))