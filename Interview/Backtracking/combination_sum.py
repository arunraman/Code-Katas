class combinationSums(object):
    def combinationSum1(self, nums, k):
        result = []
        self.combinationSum1Recursive(sorted(nums), k, 0, [], result)
        print result

    def combinationSum1Recursive(self, nums, target, start, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in xrange(start, len(nums)):
            self.combinationSum1Recursive(nums, target - nums[i], i, path + [nums[i]], res)

    def combinationSum2(self, nums, k):
        result = []
        self.combinationSum2Recursive(sorted(nums), k, 0, [], result)
        print result

    def combinationSum2Recursive(self, nums, target, start, path, res):
        if target < 0:
            return # backtracking
        if target == 0:
            res.append(path)
            return
        for i in xrange(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            self.combinationSum2Recursive(nums, target - nums[i], i + 1, path + [nums[i]], res)

    def combinationSum3(self, k, n):
        result = []
        nums = xrange(1,10)
        self.combinationSum3Recursive(nums, k, n, 0, [], result)
        print result

    def combinationSum3Recursive(self, nums, target, n, start, path, res):
        if target < 0 or n < 0:
            return # backtracking
        if target == 0 and n == 0:
            res.append(path)
            return
        for i in xrange(start, len(nums)):
            self.combinationSum3Recursive(nums, target - nums[i], n - 1, i + 1, path + [nums[i]], res )

    def combinationSum4(self, nums, k):
        # It includes the duplicates too like [1, 2, 1] and [1, 1, 2] both are valid
        memo = {0: [[]]}  # prefill value for base case of calculate_combinations where amt==0

        def combinationSum4Recursive(target):
            if target not in memo:
                memo[target] = []
                for num in nums:
                    new_amt = target - num
                    if new_amt >= 0:
                        for combination in combinationSum4Recursive(new_amt):
                            memo[target].append(combination + [num])
                            # do nothing for new_amt < 0
            return memo[target]

        return combinationSum4Recursive(k)



C = combinationSums()
C.combinationSum1([1, 2], 3)
C.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
C.combinationSum3(7, 3)
print C.combinationSum4([1, 2], 3)