# https://app.codesignal.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m
def adjacentElementsProduct(inputArray):
    max_sum = inputArray[0]
    total_sum = inputArray[0]

    if (len(inputArray) < 3):
        return inputArray[0] * inputArray[1]

    for i in range(1, len(inputArray) - 1):
        max_sum = max(inputArray[i - 1] * inputArray[i], inputArray[i + 1] * inputArray[i])
        total_sum = max(max_sum, total_sum)

    if (max_sum == 0):
        return max_sum

    return total_sum


