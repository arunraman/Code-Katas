import sys

class Treenode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):

    def addNode(self, val):
        return Treenode(val)

    def isBST(self, root):
        return self.isBSTRecu(root, -sys.maxint, sys.maxint)

    def isBSTRecu(self, root, mini, maxi):

        if root is None:
            return True

        return mini < root.val and root.val < maxi and \
               self.isBSTRecu(root.left, mini, root.val) and \
               self.isBSTRecu(root.right, root.val, maxi)


S = Solution()
root = S.addNode(1)
root.left = S.addNode(2)
root.right = S.addNode(3)
print S.isBST(root)