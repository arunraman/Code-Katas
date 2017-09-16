# Give n a list of sorted integers, find out largest integer X such that there are at
# atleast X number in the list which are >= X

# [1,2,3,3,5] - > 3

def largest_element(nums):
    for i in xrange(len(nums), 0, -1):
        if i <= sum(j >= i for j in nums):
            return i

print largest_element([1, 2, 3, 3, 5])
print largest_element([1, 4, 4])
print largest_element([1, 3, 4, 4, 4, 5])


# Given an array of length N, where array[i] is the count of ways we can produce the amount i,
# find out the set of denominations.
#
#
# input: [1, 0, 1, 0, 1, 1, 1, 2, 1, 2, 2] -> output: [2, 5, 7]

def getDenominations_1(nums):
    len_of_nums = len(nums)
    denominations = set()

    for i in xrange(1, len_of_nums):
        if nums[i] != 0:
            denominations.add(i)
            strikeMultiples(i, nums)
            if len(list(denominations)) > 1:
                sums_set = set()
                subsetSum(sums_set,list(denominations),0, len(list(denominations)) - 1)
                for x in list(sums_set):
                    if x > i and x < len_of_nums:
                        nums[x] -= 1
    print list(denominations)

def strikeMultiples(val, nums):
    original_val = val
    while (val <= len(nums)):
        if nums[val] > 0:
            nums[val] -= 1
            val += original_val

def subsetSum(sums_set, nums, left, right, sum=0):
    if left > right:
        sums_set.add(sum)
        return
    subsetSum(sums_set, nums, left + 1, right, sum + nums[left])
    subsetSum(sums_set, nums, left + 1, right, sum)

getDenominations_1([1, 0, 1, 0, 1, 1, 1, 2, 1, 2, 2])