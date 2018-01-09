class p026(object):
    def removeduplicatesfromsortedArray(self, nums):
        i = 0
        for n in nums:
            if i < 1 or n > nums[i - 1]:
                nums[i] = n
                i += 1
        return i , nums[:i]

S = p026()
print S.removeduplicatesfromsortedArray([1,1,2,2,3,4,4])