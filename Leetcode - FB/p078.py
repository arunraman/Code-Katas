class p078(object):
    def subsets(self, nums):
        return self.subsetsRecu([], sorted(nums))

    def subsetsRecu(self, curr, nums):
        if not nums:
            return [curr]
        return self.subsetsRecu(curr, nums[1:]) + self.subsetsRecu(curr + [nums[0]], nums[1:])

S = p078()
print S.subsets([1, 2, 3])