def sortinWave(nums):
    for i in xrange(0, len(nums), 2):
        if (i < 0 and nums[i] < nums[i - 1]):
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
        if (i < len(nums) - 1 and nums[i] < nums[i + 1]):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]



nums = [10, 90, 49, 2, 1, 5, 23]
sortinWave(nums)
print nums