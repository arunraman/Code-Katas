class Treenode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):

    def addNode(self, val):
        return Treenode(val)

    def lowestCommonAncestor(self, root, p, q):
        s, b = sorted([p.val, q.val])
        while not s <= root.val <= b:
            # Keep searching since root is outside of [s, b].
            root = root.left if s <= root.val else root.right
        # s <= root.val <= b.
        return root