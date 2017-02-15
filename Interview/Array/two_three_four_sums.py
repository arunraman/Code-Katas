def twoSum(nums, target):
    if len(nums) < 2:
        return False
    seen = set()
    result = set()
    for num in nums:
        val = target - num
        if val not in seen:
            seen.add(num)
        else:
            result.add((num,val))
    return list(result)


def two_sum_index(array, target):
    lookup = {}
    for index, num in enumerate(array):
        if target - num in lookup:
            return [lookup[target - num], index]
        lookup[num] = index
    return []


def threeSum(nums):
    nums = sorted(nums)
    i = 0
    result = []
    while i < len(nums) - 2:
        if i == 0 or nums[i] != nums[i-1]: # fix i position
            j = i + 1 # move j an k
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        i += 1
    return result

def threeSumClosestToTarget(nums, target):
    nums = sorted(nums)
    i = 0
    result = []
    min_diff = float("inf")
    while i < len(nums) - 2:
        if i == 0 or nums[i] != nums[i - 1]:
            j = i + 1
            k = len(nums) -1
            while j < k:
                diff = nums[i] + nums[j] + nums[k] - target
                if abs(diff) < min_diff:
                    min_diff = abs(diff)
                    result = nums[i] + nums[j] + nums[k]
                if diff < 0:
                    j += 1
                elif diff > 0:
                    k -= 1
        i += 1
    return result


def threeSumToTarget(nums, target):
    if nums is None or len(nums) < 3:
        return False
    if target is None:
        return False
    hash_map = {}
    for i in xrange(len(nums)):
        for j in xrange(i, len(nums)):
            tmp = target - (nums[i] + nums[j])
            if tmp not in hash_map:
                hash_map[tmp] = (i, j)

    for i, e in enumerate(nums):
        if e in hash_map and i not in hash_map[e]:
            return hash_map[e], i

def fourSum(nums, target):
    from collections import defaultdict
    d = defaultdict(list)
    result = set()
    for i in xrange(len(nums)):
        for j in xrange(1, len(nums)):
            val = nums[i] + nums[j]
            if val in d:
                d[val].append((i, j))
            else:
                d[val] = [(i, j)]
    for k in d:
        v = target - k
        if v in d:
            vlist = d[v]
            klist = d[k]
            for (i, j) in vlist:
                for (m, n) in klist:
                    ilist = [i ,j, m, n]
                    if len(set(ilist)) == len(ilist):
                        mylist = [nums[i], nums[j], nums[m], nums[n]]
                        mylist.sort()
                        result.add(tuple(mylist))

    return list(result)


print twoSum([-1, 0, 1, -3, -4], -4)
print two_sum_index([2, 7, 11, 15], 9)
print threeSum([-1, 0, 1, 2, -1, -4])
print threeSumClosestToTarget([-1, 2, 1, -4], 1)
print threeSumToTarget([0, 1, 5, 9, 1, 10, 11, 3, -15, -4, 2, 0, -6, 7], 2)
print fourSum([1, 0, -1, 0, -2, 2], 1)