class p015(object):

    def threeSum(self, nums):
        nums = sorted(nums)
        i = 0
        result = []
        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i - 1]:
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        result.append((nums[i], nums[j], nums[k]))
                        j += 1
                        k -= 1
            i += 1
        return result

    def threesumClosest(self, nums, target):
        nums = sorted(nums)
        i = 0
        result = []
        min_diff = float("inf")
        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i - 1]:
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    diff = nums[i] + nums[j] + nums[k] - target
                    if abs(diff) < min_diff:
                        min_diff = abs(diff)
                        result = nums[i] + nums[j] + nums[k]
                    if diff < 0:
                        j += 1
                    elif diff > 0:
                        k -= 1
            i += 1
        return result

S = p015()
print S.threeSum([-1, 0, 1, 2, -1, -4])
print S.threesumClosest([-1, 2, 1, -4], 1)
