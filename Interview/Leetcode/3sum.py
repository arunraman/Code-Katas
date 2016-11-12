def three_sum(nums):
    nums = sorted(nums)
    result = []
    i = 0
    while i < len(nums) - 2:
        if i == 0 or nums[i] != nums[i-1]:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if (nums[i] + nums[j] + nums[k]) < 0:
                    j += 1
                elif(nums[i] + nums[j] + nums[k]) > 0:
                    k -= 1
                else:
                    result.append((nums[i],nums[j],nums[k]))
                    j, k = j + 1, k - 1
        i += 1
    return result




print three_sum([-1, 0, 1, 2, -1, -4])