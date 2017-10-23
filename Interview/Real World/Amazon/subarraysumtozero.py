from collections import defaultdict

def subarraySum(nums, k = 0):
    sums = defaultdict(list)
    result_index = defaultdict(list)
    result = defaultdict(list)
    currSum = 0
    for i in xrange(len(nums)):
        currSum += nums[i]
        if currSum == k:
            result_index[k].append((0,i))
            result[k].append(nums[0:i + 1])
        elif currSum - k in sums:
            for v in sums[currSum - k]:
                result_index[k].append((v + 1, i))
                result[k].append(nums[v + 1:i + 1])
        sums[currSum].append(i)

    return result[k]

print subarraySum([1,2,-2,2,-2], 0)
print subarraySum([1, 4, 3, 2, -2, 2, 1, -1], 5)