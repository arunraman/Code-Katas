class Solution(object):

    def single_number_1(self, nums):
        return reduce(lambda x, y: x ^ y, nums)

    def single_number_2(self, nums):
        return (sum(set(nums)) * 3 - sum(nums)) / 2

    def single_number_3(self, nums):
        a = 0
        b = 0
        xor = reduce(lambda x, y: x ^ y, nums)
        mask = 1
        while (xor & mask == 0):
            mask = mask << 1
        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num
        return [a, b]



S = Solution()
print S.single_number_1([1, 1, 2, 2, 3])
print S.single_number_2([1, 1, 1, 2, 2, 2, 3])
print S.single_number_3([1, 2, 1, 3, 2, 5])