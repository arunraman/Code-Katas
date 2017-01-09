def rotate_function(nums):
    maximum = float("-inf")
    current = 0
    for i in xrange(len(nums)):
        for m, n in zip(rotate(nums, i),xrange(len(nums))):
            current += m * n
        maximum = max(current, maximum)
        current = 0
    return maximum

def rotate(array, n):
    return array[n:] + array[:n]


print rotate_function([4, 3, 2, 6])