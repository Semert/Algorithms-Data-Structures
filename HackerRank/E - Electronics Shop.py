keyboards = [3, 1]
#           40,50,60
#           5.8.12    60
usb = [5, 2, 8]
b = 10

# keyboards.sort()
# print(keyboards)
# keyboards.sort(reverse=True)
# print(keyboards)
def getMoneySpent(keyboards, usb, b):

    if min(keyboards) + min(usb) > b:
        return -1
    else:
        spend = []
        keyboards.sort(reverse=True)
        usb.sort(reverse=True)
        for i in keyboards:
            for j in usb:
                if j + i <= b:
                    spend.append(i + j)
        print(spend)
        return max(spend)


getMoneySpent(keyboards,usb,b)

