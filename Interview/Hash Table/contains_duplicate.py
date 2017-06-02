import collections
class Solution(object):

    def contains_duplicate_1(self, nums):
        return len(nums) > len(set(nums))

    # Given an array of integers and an integer k, return true if
    # and only if there are two distinct indices i and j in the array
    # such that nums[i] = nums[j] and the difference between i and j is at most k.

    def contains_duplicate_2(self, nums, k):
        lookup = collections.defaultdict(list)
        for i, num in enumerate(nums):
            if num not in lookup:
                lookup[num] = [i]
            else:
                if i - lookup[num][0] <= k:
                    return True
                lookup[num].append(i)
        print lookup
        return False

    def contains_duplicate_3(self, nums, k, t):
        if t < 0: return False
        n = len(nums)
        d = {}
        w = t + 1
        for i in xrange(n):
            m = nums[i] / w
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            d[m] = nums[i]
            if i >= k: del d[nums[i - k] / w]
        return False


S = Solution()
print S.contains_duplicate_1([1, 2, 1])
print S.contains_duplicate_2([1,2,1,3,4,5],2)