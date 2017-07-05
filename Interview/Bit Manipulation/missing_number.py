import operator

class Solution(object):
    def missingNumber(self, nums):
        return reduce(operator.xor, nums, reduce(operator.xor, xrange(len(nums) + 1)))

S = Solution()
nums = [0,1]
print S.missingNumber(nums)