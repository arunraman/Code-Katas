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

S = Solution()
root1 = Treenode(1)
root1.left = Treenode(2)
root1.right = Treenode(3)
root1.left.left = Treenode(4)
root1.left.right = Treenode(5)
print root1

root2 = Treenode(1)
root2.left = Treenode(2)
root2.right = Treenode(3)
root2.left.left = Treenode(4)
root2.left.right = Treenode(5)
print root2

if S.identical_trees(root1, root2):
    print "Trees are identical"
else:
    print "Trees are not identical"