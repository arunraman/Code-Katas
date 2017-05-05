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
    return array[-n : ] + array[ : -n]

def rotate_2(nums, k):
    from collections import deque
    d = deque(nums)
    d.rotate(k)
    print list(d)


print rotate_function([4, 3, 2, 6])

print rotate([i for i in xrange(1, 8)], 3)

rotate_2([i for i in xrange(1, 8)], 3)