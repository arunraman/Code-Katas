import sys

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) < 3 * k: return []
        sums = [0] * (len(nums) - k + 1)
        sums[0] = sum(nums[:k])
        for i in xrange(1, len(nums)-k+1):
            sums[i] = sums[i-1] + nums[i+k-1] - nums[i-1]

        dp_front = [[0, 0] for _ in xrange(len(sums))]
        dp_back = [[0, 0] for _ in xrange(len(sums))]
        dp_front_max, dp_back_max = -sys.maxint, -sys.maxint
        for i in xrange(len(sums)):
            if sums[i] > dp_front_max:
                dp_front[i] = [sums[i], i]
                dp_front_max = sums[i]
            else:
                dp_front[i] = dp_front[i-1]
        for i in xrange(len(sums) - 1, -1, -1):
            if sums[i] > dp_back_max:
                dp_back[i] = [sums[i], i]
                dp_back_max = sums[i]
            else:
                dp_back[i] = dp_back[i+1]

        ret, maxval = [], -sys.maxint
        for i in xrange(k, len(sums) - k):
            if sums[i] + dp_front[i - k][0] + dp_back[i + k][0] > maxval:
                ret = [dp_front[i - k][1], i, dp_back[i + k][1]]
                maxval = sums[i] + dp_front[i - k][0] + dp_back[i + k][0]
        return ret

S = Solution()
print S.maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2)
