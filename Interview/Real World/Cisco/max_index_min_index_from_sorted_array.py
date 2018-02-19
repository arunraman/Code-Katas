class Solution(object):
    def maxIndex(self, nums, k):
        low = 0
        high = len(nums) - 1
        result = -1
        while low <= high:
            mid = low + (high - low) / 2
            if k == nums[mid]:
                result = mid
                low = mid + 1
            elif k < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return result

    def minIndex(self, nums, k):
        low = 0
        high = len(nums) - 1
        result = -1
        while low <= high:
            mid = low + (high - low) / 2
            if k == nums[mid]:
                result = mid
                high = mid - 1
            elif k < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return result


S = Solution()
print S.maxIndex([1, 2, 2, 3, 4, 5, 5, 5, 6, 6, 6, 7], 6)
print S.maxIndex([1, 2, 2, 3], 2)

print S.minIndex([1, 2, 2, 3, 4, 5, 5, 5, 6, 6, 6, 7], 6)
print S.minIndex([1, 2, 2, 3], 2)
