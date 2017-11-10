class Treenode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def addNode(self, val):
        return Treenode(val)

    # A simple function to print leaf nodes of a Binary Tree
    def printLeaves(self, root):
        if (root):
            self.printLeaves(root.left)

            # Print it if it is a leaf node
            if root.left is None and root.right is None:
                print root.val,

            self.printLeaves(root.right)

    # A function to print all left boundary nodes, except a
    # leaf node. Print the nodes in TOP DOWN manner
    def printBoundaryLeft(self, root):
        if (root):
            if (root.left):

                # to ensure top down order, print the node
                # before calling itself for left subtree
                print root.val,
                self.printBoundaryLeft(root.left)

            elif (root.right):
                print root.val,
                self.printBoundaryRight(root.right)

                # do nothing if it is a leaf node, this way we
                # avoid duplicates in output

    # A function to print all right boundary nodes, except
    # a leaf node. Print the nodes in BOTTOM UP manner
    def printBoundaryRight(self, root):
        if (root):
            if (root.right):
                # to ensure bottom up order, first call for
                # right subtree, then print this node
                self.printBoundaryRight(root.right)
                print root.val,

            elif (root.left):
                self.printBoundaryRight(root.left)
                print root.val,

                # do nothing if it is a leaf node, this way we
                # avoid duplicates in output

    # A function to do boundary traversal of a given binary tree
    def printBoundary(self, root):
        if (root):
            print root.val,

            # Print the left boundary in top-down manner
            self.printBoundaryLeft(root.left)

            # Print all leaf nodes
            self.printLeaves(root.left)
            self.printLeaves(root.right)

            # Print the right boundary in bottom-up manner
            self.printBoundaryRight(root.right)


S = Solution()
root = S.addNode(30)
root.left = S.addNode(20)
root.right = S.addNode(40)
root.left.left = S.addNode(10)
root.left.right = S.addNode(25)
root.right.left = S.addNode(35)
root.right.right = S.addNode(50)
root.left.left.left = S.addNode(5)
root.left.left.right = S.addNode(15)
root.left.right.right = S.addNode(28)
root.right.right.left = S.addNode(41)


S.printBoundary(root)