class Treenode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):

    def addNode(self, val):
        return Treenode(val)

    def isIdentical(self, tree_1, tree_2):
        if tree_1 is None and tree_2 is None:
            return True

        if tree_1 is not None and tree_2 is not None:
            return ((tree_1.val == tree_2.val) and
                    self.isIdentical(tree_1.left, tree_2.left) and
                    self.isIdentical(tree_1.right, tree_2.right))

        return False

    def isSubtree(self, tree_1, tree_2):
        if tree_2 is None:
            return True

        if tree_1 is None:
            return True

        if self.isIdentical(tree_1, tree_2):
            return True

        return self.isSubtree(tree_1.left, tree_2) or self.isSubtree(tree_1.right, tree_2)

S = Solution()
root1 = S.addNode(30)
root1.left = S.addNode(20)
root1.right = S.addNode(40)

root2 = S.addNode(30)
root2.left = S.addNode(20)
root2.right = S.addNode(45)

print S.isSubtree(root1, root2)