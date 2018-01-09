class Treenode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def invertbinaryTree(self, root):
        if root is not None:
            root.left, root.right = \
                self.invertbinaryTree(root.right), self.invertbinaryTree(root.left)
        return root