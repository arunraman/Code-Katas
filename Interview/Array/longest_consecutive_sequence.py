import bisect
def longestIncreasingSequence(nums):
    minend = [float('inf')] * len(nums)
    for num in nums:
        minend[bisect.bisect_left(minend, num)] = num
    return bisect.bisect_left(minend, float('inf'))

def longestConsecutiveSequence(nums):
    numset, maxlen = set(nums), 0
    for n in set(nums):
        currlen, tmp = 1, n + 1
        while tmp in numset:
            currlen += 1
            numset.discard(tmp)
            tmp += 1
        tmp = n - 1
        while tmp in numset:
            currlen += 1
            numset.discard(tmp)
            tmp -= 1
        maxlen = max(maxlen, currlen)
    return maxlen

print longestIncreasingSequence([100, 4, 200, 1, 3, 2])
print longestConsecutiveSequence([100, 4, 200, 1, 3, 2])