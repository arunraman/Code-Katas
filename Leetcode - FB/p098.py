from TreeNode import TreeNode
import sys
class p098(object):

    def addNode(self, val):
        return TreeNode(val)

    def isvalidBST(self, root):
        return self.isvalidBSTRecu(root, -sys.maxint, sys.maxint)

    def isvalidBSTRecu(self, root, mini, maxi):
        if root is None:
            return True

        return mini < root.val and root.val < maxi and \
            self.isvalidBSTRecu(root.left, mini, root.val) and \
            self.isvalidBSTRecu(root.right, root.val, maxi)


S = p098()
root = S.addNode(2)
root.left = S.addNode(1)
root.right = S.addNode(3)
print S.isvalidBST(root)