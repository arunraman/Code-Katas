def nextPermutation(num):
    next, last = -1, 0
    for i in xrange(len(num) - 1):
        if num[i] < num[i + 1]:
            next = i
    if next == -1:
        num.reverse()
        return

    for i in xrange(next + 1, len(num)):
        if num[i] > num[next]:
            last = i

    num[next], num[last] = num[last], num[next]
    num[next + 1:] = num[: next :-1]


def nextPermutation_1(nums):
    i = len(nums) - 1
    while i >= 0:
        if nums[i] > nums[i - 1]:
            i -= 1

num = [1, 2, 3]
nextPermutation(num)
print num
nextPermutation(num)
print num
nextPermutation(num)
print num

nums = [1, 2, 3]
nextPermutation_1(nums)