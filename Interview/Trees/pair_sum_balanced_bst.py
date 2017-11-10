# Definition for a binary tree node.
class Treenode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.pairs = set()

    def addNode(self, data):
        return Treenode(data)

    def findTarget(self, root, k):
        if not root: return False
        bfs, s = [root], set()
        for i in bfs:
            if k - i.val in s:
                self.pairs.add((i.val, k - i.val))
            s.add(i.val)
            if i.left: bfs.append(i.left)
            if i.right: bfs.append(i.right)
        return list(self.pairs)


S = Solution()
root = S.addNode(15)
root.left = S.addNode(10)
root.right = S.addNode(20)
root.left.left = S.addNode(8)
root.left.right = S.addNode(12)
root.right.left = S.addNode(-1)
root.right.right = S.addNode(21)

print S.findTarget(root, 20)