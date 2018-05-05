from binarytree import Node as TN
class Solution(object):

    def create_tree(self, nums, root, i):
        if i < len(nums):
            root = TN(nums[i])
            root.left = self.create_tree(nums, root.left, 2 * i + 1)
            root.right = self.create_tree(nums, root.right, 2 * i + 2)
        return root


S = Solution()
nums = [7, 3, 9, 2, 4, 8, 10]
root = None
print S.create_tree(nums, root, 0)