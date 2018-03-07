from binarytree import Node as Treenode

class Solution(object):
    def identical_trees(self, tree_1, tree_2):
        if tree_1 is None and tree_2 is None:
            return True

        if tree_1 is not None and tree_2 is not None:
            return ((tree_1.value == tree_2.value) and
                    self.identical_trees(tree_1.left, tree_2.left) and
                    self.identical_trees(tree_1.right, tree_2.right))

        return False

    def isSubtree(self, s, t):
        if not s:
            return False
        if self.identical_trees(s, t):
            return True
        if self.isSubtree(s.left, t) or self.isSubtree(s.right, t):
            return True
        return False

S = Solution()
root1 = Treenode(30)
root1.left = Treenode(20)
root1.right = Treenode(40)
root1.left.left = Treenode(20)
root1.left.right = Treenode(40)
print root1

root2 = Treenode(20)
root2.left = Treenode(20)
root2.right = Treenode(40)
print root2

print S.isSubtree(root1, root2)