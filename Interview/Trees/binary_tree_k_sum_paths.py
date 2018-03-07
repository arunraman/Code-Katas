from binarytree import Node as Treenode


class Solution(object):
    def __init__(self):
        self.path = []

    def k_path_sum(self, root, k):
        if root is None:
            return
        #print 'Visiting {}'.format(root.value)
        self.path.append(root.value)
        self.k_path_sum(root.left, k)
        self.k_path_sum(root.right, k)
        #print 'Current path: {}'.format(self.path)
        currsum = 0
        for i in reversed(xrange(len(self.path))):
            currsum += self.path[i]
            if currsum == k:
                print self.path[i:]
        self.path.pop()

root = Treenode(1)
root.left = Treenode(3)
root.left.left = Treenode(2)
root.left.right = Treenode(1)
root.left.right.left = Treenode(1)
root.right = Treenode(-1)
root.right.left = Treenode(4)
root.right.left.left = Treenode(1)
root.right.left.right = Treenode(2)
root.right.right = Treenode(5)
root.right.right.right = Treenode(2)
print(root)

S = Solution()
S.k_path_sum(root, 5)