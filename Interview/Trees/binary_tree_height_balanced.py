class Treenode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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

root = S.addNode(1)
root.left = S.addNode(2)
root.right = S.addNode(3)
root.left.left = S.addNode(4)
root.left.left.left = S.addNode(5)

print S.isheightBalanced(root)