# https://www.hackerrank.com/challenges/append-and-delete/problem
def appendAndDelete(s, t, k):
    sl ,tl , c =len(s) ,len(t) ,0
    if k>= sl + tl or s == t: return "Yes"
    for i in range(min(sl, tl)):
        if s[i] == t[i]:
            c += 1
        else:
            break
    sl -= c;
    tl -= c
    if sl < tl and (k - tl) % 2 == 0:
        return "Yes"

    elif sl > tl and (k - sl) % 2 == 0:
        return "Yes"
    else:
        return "No"