class Treenode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):

    def addNode(self, val):
        return Treenode(val)

    def storeInorder(self, root, inorder):

        # Base Case
        if root is None:
            return

        # First store the left subtree
        self.storeInorder(root.left, inorder)

        # Copy the root's val
        inorder.append(root.val)

        # Finally store the right subtree
        self.storeInorder(root.right, inorder)

    # Helper function that copies contents of sorted array
    # to Binary tree
    def arrayToBST(self, arr, root):

        # Base Case
        if root is None:
            return

        # First update the left subtree
        self.arrayToBST(arr, root.left)

        # now update root's val delete the value from array
        root.val = arr[0]
        arr.pop(0)

        # Finally update the right subtree
        self.arrayToBST(arr, root.right)

    # This function converts a given binary tree to BST
    def binaryTreeToBST(self, root):

        # Base Case: Tree is empty
        if root is None:
            return

        # Create the temp array and store the inorder traveral
        # of tree
        arr = []
        self.storeInorder(root, arr)

        # Sort the array
        arr.sort()

        # copy array elements back to binary tree
        self.arrayToBST(arr, root)

    # Print the inorder traversal of the tree
    def printInorder(self, root):
        if root is None:
            return
        self.printInorder(root.left)
        print root.val,
        self.printInorder(root.right)

S = Solution()
root = S.addNode(10)
root.left = S.addNode(30)
root.right = S.addNode(15)
root.left.left = S.addNode(20)
root.right.right= S.addNode(5)

S.binaryTreeToBST(root)
S.printInorder(root)