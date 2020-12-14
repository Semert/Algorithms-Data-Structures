def alphabeticShift(inputString):
    a = ""

    for i in inputString:
        if i != "z":
            a += chr(ord(i) + 1)
        else:
            a += "a"

    return a


