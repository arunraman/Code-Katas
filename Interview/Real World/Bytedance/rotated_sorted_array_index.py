"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1

"""


class Solution:
    def searchrotatedsortedarray(self, nums, target):
        n = len(nums)
        if n == 0:
            return -1
        lo, hi, mid, = (
            0,
            n - 1,
            0,
        )
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if (nums[mid] < nums[0]) ^ (target < nums[0]):
                if target < nums[0]:
                    nums[mid] = float("-inf")
                else:
                    nums[mid] = float("inf")

            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1


S = Solution()
print(
    S.searchrotatedsortedarray(
        [12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 14
    )
)
