# https://app.codesignal.com/arcade/intro/level-5/veW5xJednTy4qcjso/solutions

def isIPv4Address(s):

    # p = s.split('.')
    # return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p)

    sl = s.split('.')
    if len(sl) != 4:
        return False

    for s in sl:
        if not s.isdigit():
            return False;
        a = int(s)
        if a > 255 or a < 0:
            return False

        if len(s) == 2 and s[0] == "0":
            return False

    return True;





