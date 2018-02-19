class Solution(object):
    def moveZeros(self, nums):
        if len(nums) < 1 or len(nums) == 1:
            return nums
        start = 0
        end = len(nums) - 1
        while start <= end:
            if nums[start] == 0 and nums[end] != 0:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            elif nums[start] == 0 and nums[end] == 0:
                end -= 1
            else:
                start += 1
        return nums

S = Solution()
print S.moveZeros([0, 1, 2, 0, 4, 0])
print S.moveZeros([0, 0, 0])
print S.moveZeros([1])