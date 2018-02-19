class p090(object):
    def subsetswithDup(self, nums):
        result = []
        self.subsetswithdupRecursive(result, [], sorted(nums))
        return result

    def subsetswithdupRecursive(self, result, curr, nums):
        if not nums:
            if curr not in result:
                result.append(curr)
        else:
            self.subsetswithdupRecursive(result, curr, nums[1:])
            self.subsetswithdupRecursive(result, curr + [nums[0]], nums[1:])

S = p090()
print S.subsetswithDup([1, 2, 2])