class Treenode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):

    def addNode(self, val):
        return Treenode(val)

    def isValidBST(self, root):
        return self.isValidBSTRecu(root, float("-inf"), float("inf"))


    def isValidBSTRecu(self, root, low, high):
        if root is None:
            return True

        return low < root.val and root.val < high \
               and self.isValidBSTRecu(root.left, low, root.val) \
               and self.isValidBSTRecu(root.right, root.val, high)


S = Solution()
root = S.addNode(10)
root.left = S.addNode(5)
root.right = S.addNode(15)
print S.isValidBST(root)