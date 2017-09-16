def maxSlidingWindow(arr, N):
    slidingMax = []
    for i in xrange(len(arr)):
        if i >= N-1:
            slidingMax.append(getMax(arr, i, N))
    return slidingMax


def getMax(arr, index, N):
    index_count = 0
    temp = []
    while (index_count != N):
        temp.append(arr[index])
        index -= 1
        index_count += 1
    return max(temp)


print maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
