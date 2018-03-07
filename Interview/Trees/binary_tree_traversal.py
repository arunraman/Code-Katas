from binarytree import Node as Treenode

class Solution():
    def preOrder(self, root):
        if root == None:
            return
        print root.value,
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):
        if root == None:
            return
        self.inOrder(root.left)
        print root.value,
        self.inOrder(root.right)

    def postOrder(self, root):
        if root == None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print root.value,

S = Solution()
root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
root.left.left = Treenode(8)
root.left.right = Treenode(12)
root.right.left = Treenode(3)
root.right.right = Treenode(25)
print root
S.preOrder(root)
print "\n"
S.inOrder(root)
print "\n"
S.postOrder(root)