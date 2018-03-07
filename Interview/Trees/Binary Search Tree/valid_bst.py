import sys
from binarytree import Node as TN

class Solution(object):

    def isBST(self, root):
        return self.isBSTRecu(root, -sys.maxint, sys.maxint)

    def isBSTRecu(self, root, mini, maxi):

        if root is None:
            return True

        return mini < root.value and root.value < maxi and \
               self.isBSTRecu(root.left, mini, root.value) and \
               self.isBSTRecu(root.right, root.value, maxi)


S = Solution()
root = TN(1)
root.left = TN(2)
root.right = TN(3)
print root.preorder
print root.inorder
print root.postorder
print(root)
print S.isBST(root)