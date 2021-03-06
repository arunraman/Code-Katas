class Solution(object):
    def searchRange(self, nums, target):
        def search(lo, hi):
            if nums[lo] == target == nums[hi]:
                return [lo, hi]
            if nums[lo] <= target <= nums[hi]:
                mid = (lo + hi) / 2
                l, r = search(lo, mid), search(mid + 1, hi)
                return max(l, r) if -1 in l + r else [l[0], r[1]]
            return [-1, -1]

        return search(0, len(nums) - 1)


S = Solution()
print S.searchRange([5, 7, 7, 8, 8, 10], 8)