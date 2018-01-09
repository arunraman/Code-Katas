class p001(object):

    def twoSum(self, nums, target):
        if len(nums) < 2:
            return False
        result = set()
        seen = dict()
        for i in xrange(len(nums)):
            val = target - nums[i]
            if val in seen and seen[val] != i:
                result.add((i, seen[val]))
            seen[nums[i]] = i
        return result


S = p001()
print S.twoSum([2, 7, 11, 15], 9)
