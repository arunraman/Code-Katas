from binarytree import Node as Treenode


class Solution(object):
    def addNode(self, val):
            return Treenode(val)

    def maxHeight(self, root):
        if not root:
            return 0
        else:
            return max(self.maxHeight(root.left),
                       self.maxHeight(root.right)) + 1

    def isheightBalanced(self, root):
        if root == None:
            return True
        if self.maxHeight(root.left) - self.maxHeight(root.right) <= 1:
            return self.isheightBalanced(root.left) and self.isheightBalanced(root.right)
        else:
            return False

S = Solution()

root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
root.left.left = Treenode(4)
root.right.right = Treenode(5)

print root
print S.maxHeight(root)
print S.isheightBalanced(root)