class Treenode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):

    def addNode(self, val):
        return Treenode(val)

    def isSubtree(self, s, t):

        def check(s, t):
            # helper function that does the actual subtree check
            if (s is None) and (t is None):
                return True
            if (s is None) or (t is None):
                return False
            return (s.val == t.val and check(s.left, t.left) and check(s.right, t.right))

        # need to do a pre-order traversal and do a check
        # for every node we visit for the subtree
        if not s:
            # return False since None cannot contain a subtree
            return False
        if check(s, t):
            # we found a match
            return True
        if self.isSubtree(s.left, t) or self.isSubtree(s.right, t):
            # a match was found
            return True
        return False

S = Solution()
root1 = S.addNode(30)
root1.left = S.addNode(20)
root1.right = S.addNode(40)

root2 = S.addNode(30)
root2.left = S.addNode(20)
root2.right = S.addNode(40)

print S.isSubtree(root1, root2)