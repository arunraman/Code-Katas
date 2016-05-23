def minMaxDifference(inputArray):

    indexOfMinimum = 0
    indexOfMaximum = 0

    for i in range(1, len(inputArray)):
        if inputArray[i] < inputArray[indexOfMinimum]:
            indexOfMinimum = i
        if inputArray[i] > inputArray[indexOfMaximum]:
            indexOfMaximum = i
    return inputArray[indexOfMaximum] - inputArray[indexOfMinimum]


input  = [32, 19, 11, 23]
print minMaxDifference(input)