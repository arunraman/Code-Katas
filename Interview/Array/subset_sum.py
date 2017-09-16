

def subsetSum(sums_set, nums, left, right, sum=0):
    if left > right:
        sums_set.add(sum)
        return
    subsetSum(sums_set, nums, left + 1, right, sum + nums[left])
    subsetSum(sums_set, nums, left + 1, right, sum)

nums = [1, 2, 3]
sums_set = set() # Replaces this with array if we want duplicate sums too
subsetSum(sums_set, nums, 0, len(nums) -1)
print list(sums_set)