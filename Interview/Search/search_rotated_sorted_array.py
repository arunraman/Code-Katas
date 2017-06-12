class Solution():

    def searchrotatedsortedarray(self, nums, target):
        n = len(nums)
        if n == 0:
            return -1
        lo , hi, mid, = 0 ,n - 1, 0
        while (lo <= hi):
            mid = (lo + hi) >> 1
            if (nums[mid] == target):
                return mid
            if ((nums[mid] < nums[0]) ^ (target < nums[0])):
                if target < nums[0]:
                    nums[mid] = float("-inf")
                else:
                    nums[mid] = float("inf")

            if (nums[mid] < target):
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

S = Solution()
print S.searchrotatedsortedarray([12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 14)