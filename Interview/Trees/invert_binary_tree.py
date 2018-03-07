from binarytree import Node as TN

class Solution(object):
    def invertbinaryTree(self, root):
        if root is not None:
            root.left, root.right = \
                self.invertbinaryTree(root.right), self.invertbinaryTree(root.left)
        return root

S = Solution()

root = TN(4)
root.left = TN(2)
root.left = TN(2)
root.right = TN(7)
root.left.left = TN(1)
root.left.right = TN(3)
root.right.left = TN(6)
root.right.right = TN(9)

print root

print S.invertbinaryTree(root)