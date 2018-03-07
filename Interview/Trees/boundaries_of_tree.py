from binarytree import Node as Treenode


class Solution(object):
    # A simple function to print leaf nodes of a Binary Tree
    def printLeaves(self, root):
        if (root):
            self.printLeaves(root.left)

            # Print it if it is a leaf node
            if root.left is None and root.right is None:
                print root.value,

            self.printLeaves(root.right)

    # A function to print all left boundary nodes, except a
    # leaf node. Print the nodes in TOP DOWN manner
    def printBoundaryLeft(self, root):
        if (root):
            if (root.left):

                # to ensure top down order, print the node
                # before calling itself for left subtree
                print root.value,
                self.printBoundaryLeft(root.left)

            elif (root.right):
                print root.value,
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
                print root.value,

            elif (root.left):
                self.printBoundaryRight(root.left)
                print root.value,

                # do nothing if it is a leaf node, this way we
                # avoid duplicates in output

    # A function to do boundary traversal of a given binary tree
    def printBoundary(self, root):
        if (root):
            print root.value,

            # Print the left boundary in top-down manner
            self.printBoundaryLeft(root.left)

            # Print all leaf nodes
            self.printLeaves(root.left)
            self.printLeaves(root.right)

            # Print the right boundary in bottom-up manner
            self.printBoundaryRight(root.right)


S = Solution()
root = Treenode(30)
root.left = Treenode(20)
root.right = Treenode(40)
root.left.left = Treenode(10)
root.left.right = Treenode(25)
root.right.left = Treenode(35)
root.right.right = Treenode(50)
root.left.left.left = Treenode(5)
root.left.left.right = Treenode(15)
root.left.right.right = Treenode(28)
root.right.right.left = Treenode(41)
print root

S.printBoundary(root)