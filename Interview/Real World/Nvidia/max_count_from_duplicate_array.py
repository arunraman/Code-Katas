from collections import defaultdict

class Solution(object):
    def getMaxrepetitions(self, nums):
        currmax = 0
        countDict = defaultdict(list)
        seen = defaultdict(int)
        for i in xrange(len(nums)):
            seen[nums[i]] += 1
            countDict[seen[nums[i]]].append(nums[i])
            currmax = max(seen[nums[i]], currmax)
        print currmax, countDict[currmax]



S = Solution()
S.getMaxrepetitions([1,2,3,3,2,5,1,6,2,3,1,2,1])