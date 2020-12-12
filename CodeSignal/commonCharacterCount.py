# https://app.codesignal.com/arcade/intro/level-3/JKKuHJknZNj4YGL32
def commonCharacterCount(s1, s2):
    arr = []

    for i in set(s1):
        arr.append(min(s1.count(i), s2.count(i)))

    return (sum(arr))




