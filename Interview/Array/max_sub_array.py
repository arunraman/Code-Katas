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
    from collections import defaultdict
    sums = {}
    result = defaultdict(list)
    cur_sum, max_len = 0, 0
    for i in xrange(len(nums)):
        cur_sum += nums[i]
        if cur_sum == k:
            max_len = i + 1
            result[k].append(nums[:i+1])
        elif cur_sum - k in sums:
            max_len = max(max_len, i - sums[cur_sum - k])
            result[k].append(nums[sums[cur_sum - k] + 1: i + 1])
        if cur_sum not in sums:
            sums[cur_sum] = i  # Only keep the smallest index.

    if max_len:
        return max_len, result.values()[0]
    else:
        return "No Sub-array found"

print SubArraySumtoTarget([1, 4, 3, 2, 1, -1], 5)
print SubArraySumtoTarget([-1, -4, -3, -2, -1, -1], 5)
