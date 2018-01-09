class Treenode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):

    def addNode(self, val):
        return Treenode(val)

    def lowestCommonAncestor(self, root, p, q):
            if root in (None, p, q):
                return root

            left, right = [self.lowestCommonAncestor(child, p, q)
                          for child in (root.left, root.right)]
            # 1. If the current subtree contains both p and q,
            #    return their LCA.
            # 2. If only one of them is in that subtree,
            #    return that one of them.
            # 3. If neither of them is in that subtree,
            #    return the node of that subtree.
            return root if left and right else left or right

S = Solution()

root = S.addNode(30)
root.left = S.addNode(20)
root.right = S.addNode(40)
root.left.left = S.addNode(10)
root.left.right = S.addNode(15)
root.right.right = S.addNode(5)

print S.lowestCommonAncestor(root, root.left.left, root.left.right).val