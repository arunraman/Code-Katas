from collections import namedtuple

Result = namedtuple("Result", "maxSum maxTop maxDown maxLeft maxRight")

KadaneResult = namedtuple("KadaneResult", "maxSum maxStart maxEnd")

def kadane(nums):
    currSum = 0
    currStart = 0
    maxStart = 0
    maxEnd= 0
    maxSum = 0

    if len(nums) < 2:
        return nums

    if sum(1 for val in nums if val < 0) == len(nums): # if everything is negative return the max
        best = max(nums)
        return best, nums[nums.index(best)]

    for ind, val in enumerate(nums):
        if currSum + val > 0:
            currSum += val
        else:
            currSum = 0
            currStart = ind + 1

        if currSum > maxSum:
            maxStart = currStart
            maxEnd = ind + 1
            maxSum = currSum

    return KadaneResult(maxSum, maxStart, maxEnd)


def max_sub_rectangle_sum(grid):
    rows = len(grid)
    cols = len(grid[0])

    result = Result(float("-inf"), -1, -1, -1, -1)

    for left in xrange(cols):
        temp = [0 for _ in xrange(cols)]
        for right in xrange(left, cols):
            for i in xrange(rows):
                temp[i] += grid[i][right]
                print temp

            kadane_result = kadane(temp)
            if kadane_result.maxSum > result.maxSum:
                result = Result(kadane_result.maxSum, left, right, kadane_result.maxStart, kadane_result.maxEnd)

    print result


grid = [[1, 0, 0],
        [1, 0, 0],
        [1, 0, 0]]

max_sub_rectangle_sum(grid)


