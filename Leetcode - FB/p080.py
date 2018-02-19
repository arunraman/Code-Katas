class p080(object):
    def removeduplicatesfromsortedarrayallowedTwice(self, nums):
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
        return i, nums[:i]
S = p080()
print S.removeduplicatesfromsortedarrayallowedTwice([1, 1, 1, 2, 2, 3])