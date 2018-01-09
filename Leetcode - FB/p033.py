class p033(object):
    def searchinrotatedsortedArray(self, nums, target):
        lo = 0
        hi = len(nums) - 1
        while (lo <= hi):
            mid = lo + hi / 2
            if nums[mid] == target: return mid
            if nums[lo] == target: return lo
            if nums[lo] < nums[mid]:
                if (target < nums[mid] and target > nums[lo]):
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if (target < nums[lo] and target > nums[mid]):
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1


S = p033()
print S.searchinrotatedsortedArray([4, 5, 6, 7, 0, 1, 2], 6)
