class p075(object):
    #dutch national flag
    def sortColors(self, nums):
        high = len(nums) - 1
        ptr1 = 0
        ptr2 = 0
        while ptr1 <= high:
            if nums[ptr1] == 0:
                nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
                ptr1 += 1
                ptr2 += 1
            elif nums[ptr2] == 2:
                nums[ptr1], nums[high] = nums[high], nums[ptr1]
                high = high - 1
            else:
                ptr1 += 1
        return nums

S = p075()
print S.sortColors([0, 1, 2, 2, 0, 1])