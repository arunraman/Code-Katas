class Treenode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def addNode(self, val):
            return Treenode(val)

    def roottoleafpathSum(self, root, s):
        if root == None:
            return s == 0
        else:
            ans = 0

            # Otherwise check both subtrees
            subSum = s - root.val

            # If we reach a leaf node and sum becomes 0, then
            # return True
            if (subSum == 0 and root.left == None and root.right == None):
                return True

            if root.left is not None:
                ans = ans or self.roottoleafpathSum(root.left, subSum)
            if root.right is not None:
                ans = ans or self.roottoleafpathSum(root.right, subSum)

            return ans



S = Solution()
s = 21
root = S.addNode(10)
root.left = S.addNode(8)
root.right = S.addNode(2)
root.left.right = S.addNode(5)
root.left.left = S.addNode(3)
root.right.left = S.addNode(2)
print S.roottoleafpathSum(root, s)