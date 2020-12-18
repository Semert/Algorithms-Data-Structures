# https://app.codesignal.com/arcade/intro/level-1/s5PbmwxfECC52PWyQ
def checkPalindrome(inputString):
    left = 0
    right = len(inputString) - 1

    while left <= right:

        if (inputString[left] == inputString[right]):
            left += 1
            right -= 1
        else:
            return False

    return True


