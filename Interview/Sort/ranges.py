class Solution():
    def findMissingRanges(self, nums, lower, upper):
        result = []
        start = lower - 1
        for i in xrange(len(nums) + 1):
            if i == len(nums):
                end = upper + 1
            else:
                end = nums[i]
            if end - start >= 2:
                result.append(self.range(start + 1, end - 1))
            start = end
        print result


    def summaryRanges(self, nums):
        if not nums:
            return []
        result = []
        start, end = 0, 0
        for i in xrange(1, len(nums)):
            if nums[i] - nums[i - 1] != 1:
                result.append(self.range(start, end))
                start = nums[i]
            end = nums[i]
        result.append(self.range(start, end))
        print result


    def range(self, start, end):
        if start == end:
            return str(start)
        else:
            return str(start) + "->" + str(end)


Solution().findMissingRanges([0, 1], 0, 99)
Solution().summaryRanges([0, 1, 2, 4])