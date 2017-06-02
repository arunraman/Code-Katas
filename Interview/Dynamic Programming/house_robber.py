class Solution():

    def house_robber_1(self, nums):
        prev, now = 0, 0
        for n in nums:
            prev, now = now, max(prev + n, now)
        return now

    def house_robber_2(self, nums):
        def rob(nums):
            now = prev = 0
            for n in nums:
                now, prev = max(now, prev + n), now
            return now

        return max(rob(nums[len(nums) != 1:]), rob(nums[:-1]))

S = Solution()
print S.house_robber_1([12,2,10,1])
print S.house_robber_2([8,4,8,9,10])