import bisect
def longestIncreasingSequence(nums):
    minend = [float('inf')] * len(nums)
    for num in nums:
        minend[bisect.bisect_left(minend, num)] = num
    return bisect.bisect_left(minend, float('inf'))

def longestConsecutive(nums):
    nums = nums
    best = 0
    result = set()
    for x in nums:
        if x - 1 not in nums:

            y = x + 1
            while y in nums:
                result.add(x)
                result.add(y)
                y += 1
            best = max(best, y - x)
    return best, list(result)

print longestIncreasingSequence([100, 4, 200, 1, 3, 2])
print longestConsecutive([100, 4, 200, 1, 3, 2])