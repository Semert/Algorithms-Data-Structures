def arrayReplace(inputArray, elemToReplace, substitutionElem):
    # return [substitutionElem if i == elemToReplace else i for i in inputArray]
    arr = []
    for i in inputArray:
        if i == elemToReplace:
            arr.append(substitutionElem)
        else:
            arr.append(i)

    return arr




