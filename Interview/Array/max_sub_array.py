from collections import defaultdict

# Maximum sum sub-array with the array elements2
def max_sum_sub_array(array):
    if len(array) < 2:
        return array

    if sum(1 for val in array if val < 0) == len(array): # if everything is negative return the max
        best = max(array)
        return best, array[array.index(best)]

    best = cur = 0
    curi = starti = endi = 0
    for ind, val in enumerate(array):
        if cur + val > 0:
            cur += val
        else:
            cur = 0
            curi = ind + 1

        if cur > best:
            starti = curi
            endi = ind + 1
            best = cur

    return best, array[starti:endi]

print max_sum_sub_array([-2,1,-3,4,-1,2,1,-5,4])
print max_sum_sub_array([-1, -4, -5, -9])


def max_sum_sub_array_1(array):
    if len(array) < 2:
        return array
    current = best = 0
    for x in array:
        current = max(x, current + x)
        best = max(best, current)
    return best

print max_sum_sub_array_1([1, 4, -5, -9])


def min_sum_sub_array_1(array):
    if len(array) < 2:
        return array
    current = best = 0
    for x in array:
        current = min(x, current + x)
        best = min(best, current)
    return best

print min_sum_sub_array_1([1, 4, -5, -9])

def min_sum_sub_array_to_target(array, k):
    start = 0
    current_sum = 0
    min_len = float("inf")
    for i in xrange(len(array)):
        current_sum += array[i]
        while current_sum >= k:
            min_len = min(min_len, i - start + 1)
            current_sum -= array[start]
            start += 1

    return min_len if min_len != float("inf") else 0

print min_sum_sub_array_to_target([2,3,1,2,4,3], 7)

def SubArraySumtoTarget(nums, k):
    sums = defaultdict(list)
    result_index = defaultdict(list)
    result = defaultdict(list)
    currSum = 0
    for i in xrange(len(nums)):
        currSum += nums[i]
        if currSum == k:
            result_index[k].append((0, i))
            result[k].append(nums[0:i + 1])
        elif currSum - k in sums:
            for v in sums[currSum - k]:
                result_index[k].append((v + 1, i))
                result[k].append(nums[v + 1:i + 1])
        sums[currSum].append(i)

    if result:
        return result[k]
    else:
        return "No Sub-array found"

print SubArraySumtoTarget([1, 4, 3, 2, -2, 2, 1, -1], 5)
print SubArraySumtoTarget([1,2,-2,2,-2], 0)
