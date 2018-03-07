from binarytree import Node as TN

class Solution(object):
    def sortedarraytoBST(self, nums):
        return self.sortedarraytoBSTrecu(nums, 0, len(nums) - 1)

    def sortedarraytoBSTrecu(self, nums, begin, end):
        if begin > end:
            return None
        mid = begin + (end - begin) // 2
        root = TN(nums[mid])
        root.left = self.sortedarraytoBSTrecu(nums, begin, mid - 1)
        root.right = self.sortedarraytoBSTrecu(nums, mid + 1, end)
        return root

S = Solution()
print S.sortedarraytoBST([1, 2, 3, 4, 5])