# https://app.codesignal.com/arcade/intro/level-6/PWLT8GBrv9xXy4Dui

def alphabeticShift(inputString):
    a = ""

    for i in inputString:
        if i != "z":
            a += chr(ord(i) + 1)
        else:
            a += "a"

    return a


