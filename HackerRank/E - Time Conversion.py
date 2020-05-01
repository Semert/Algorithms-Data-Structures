
# https: // www.hackerrank.com / challenges / time - conversion / problem


def timeConversion(s):
    s1 = list(s[:-1].split(":"))
    last = str(s1[2])
    if int(s1[0]) < 12:
        if last[-1] == "P":
            s1[0] = str(int(s1[0]) + 12)
    else:
        if last[-1] == "A" and int(s1[0]) == 12:
            s1[0] = "00"

    s1[2] = last[0:2]
    s1 = ':'.join(map(str, s1))
    return s1
    # Solution 2
    l = list(s)
    val = l[-2]
    value = int(l[0] + l[1])
    if (val == "A" and value != 12) or (val == "P" and value == 12):
        res = "".join(l)
    elif val == "A" and value == 12:
        l[0] = "0"
        l[1] = "0"
        res = "".join(l)
    else:
        value = str(value + 12)
        l[0] = value[0]
        l[1] = value[1]

        res = "".join(l)
    return res[0:-2]