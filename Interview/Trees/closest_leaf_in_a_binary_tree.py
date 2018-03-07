import sys
from binarytree import Node as Treenode

class Solution(object):
    def closestDown(self, root):
        #Base Case
        if root is None:
            return sys.maxint
        if root.left is None and root.right is None:
            return 0

        # Return minum of left and right plus one
        return 1 + min(self.closestDown(root.left),
                       self.closestDown(root.right))

        # Returns destance of the closes leaf to a given key k
        # The array ancestors us used to keep track of ancestors
        # of current node and 'index' is used to keep track of
        # current index in 'ancestors[i]'
    def findClosestUtil(self, root, k, ancestors, index):
        # Base Case
        if root is None:
            return sys.maxint

        # if key found
        if root.key == k:
            # Find closest leaf under the subtree rooted
            # with given key
            res = self.closestDown(root)

            # Traverse ll ancestors and update result if any
            # parent node gives smaller distance
            for i in reversed(range(0,index)):
                res = min(res, index-i+self.closestDown(ancestors[i]))
            return res

        # if key node found, store current node and recur for left
        # and right childrens
        ancestors[index] = root
        return min(
            self.findClosestUtil(root.left, k,ancestors, index+1),
            self.findClosestUtil(root.right, k, ancestors, index+1))

    # The main function that return distance of the clses key to
    # 'key'. It mainly uses recursive function findClosestUtil()
    # to find the closes distance
    def findClosest(self, root, k):
        # Create an arrray to store ancestors
        # Assumption: Maximum height of tree is 100
        ancestors = [None for i in range(100)]

        return self.findClosestUtil(root, k, ancestors, 0)

root = Treenode(2)
root.left = Treenode(5)
root.right = Treenode(3)
print root

S = Solution()
print S.closestDown(root)