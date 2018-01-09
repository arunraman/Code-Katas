class Treenode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):

    def addNode(self, data):
        return Treenode(data)

    def isSymmetric(self, root):
        if root is None:
            return True
        return self.issymmetricRecursive(root.left, root.right)

    def issymmetricRecursive(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.issymmetricRecursive(left.left, right.right) and \
               self.issymmetricRecursive(left.right, right.left)


S = Solution()
root = S.addNode(1)
root.left, root.right = S.addNode(2), S.addNode(2)
root.left.left, root.right.right = S.addNode(3), S.addNode(3)
root.left.right, root.right.left = S.addNode(4), S.addNode(4)
print Solution().isSymmetric(root)