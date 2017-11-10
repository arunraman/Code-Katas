from collections import defaultdict


def longestIncreasingConsecutiveSubarray(nums):
    longest_dict = defaultdict(list)
    if not nums:
        return 0
    if len(nums) == 1:
        return 1
    start, end, max_len = 0, 1, 1
    while end < len(nums):
        if nums[end] > nums[end - 1]:
            max_len = max(max_len, end - start + 1)
        else:
            longest_dict[max_len].append(nums[start:end])
            start = end
        end += 1

    # Get the tail too
    longest_dict[end - start].append(nums[start:end])

    return longest_dict[max_len]

print longestIncreasingConsecutiveSubarray([100, 1, 50, 99, 2, 3, 1000, 1001])
print longestIncreasingConsecutiveSubarray([1, 3, 2, 4, 5, 6, 2, 3])


# this is also the bridges and cities problem
def longestIncreasingSequence(nums):
    l = []
    for i in range(len(nums)):
        l.append(max([l[j] for j in range(i) if l[j][-1] < nums[i]] or [[]], key=len)
                 + [nums[i]])
    return max(l, key=len)


print longestIncreasingSequence([10, 9, 2, 5, 3, 7, 101, 18])
print longestIncreasingSequence([100, 1, 50, 99, 2, 3, 1000, 1001])


def longestConsecutiveSequence(nums):
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

print longestConsecutiveSequence([100, 4, 200, 1, 3, 2])
print longestConsecutiveSequence([3, 7, 9, 4, 12, 2, 1, 5])