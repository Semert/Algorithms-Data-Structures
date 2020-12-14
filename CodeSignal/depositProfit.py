# https://app.codesignal.com/arcade/intro/level-7/8PxjMSncp9ApA4DAb
def depositProfit(deposit, rate, threshold):
    year = 0
    while deposit < threshold:
        deposit += deposit * rate/100
        year += 1
    return year