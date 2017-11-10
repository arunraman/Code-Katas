def rearrange_array(nums):
    for i in xrange(len(nums)):
        nums[i] += (nums[nums[i]] % len(nums)) * len(nums)

    for i in xrange(len(nums)):
        nums[i] /= len(nums)

    print nums

rearrange_array([3, 2, 0, 1])