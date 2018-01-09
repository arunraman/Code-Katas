import collections

class Treenode():
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def addNode(self, data):
        return Treenode(data)

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        def getid(root, lookup, trees):
            if root:
                node_id = lookup[root.val, \
                                 getid(root.left, lookup, trees), \
                                 getid(root.right, lookup, trees)]
                trees[node_id].append(root)
                return node_id
        trees = collections.defaultdict(list)
        lookup = collections.defaultdict()
        lookup.default_factory = lookup.__len__
        getid(root, lookup, trees)
        return [roots[0] for roots in trees.values() if len(roots) > 1]

S = Solution()
root = S.addNode(1)
root.left = S.addNode(2)
root.right = S.addNode(3)
root.left.left = S.addNode(4)
root.right.left = S.addNode(2)
root.right.right = S.addNode(4)
root.right.left.left = S.addNode(4)

print S.findDuplicateSubtrees(root)
