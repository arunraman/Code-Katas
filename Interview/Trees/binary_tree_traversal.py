class Treenode():
    def __init__(self, x=None):
        self.value = x
        self.left = None
        self.right = None

class Solution():
    def __init__(self):
        self.stack = []

    def addNode(self, data):
        return Treenode(data)

    def preOrder(self, root):
        if root == None:
            return
        print root.value
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):
        if root == None:
            return
        self.preOrder(root.left)
        print root.value
        self.preOrder(root.right)

    def postOrder(self, root):
        if root == None:
            return
        self.preOrder(root.left)
        self.preOrder(root.right)
        print root.value

S = Solution()
root = S.addNode(15)
root.left = S.addNode(10)
root.right = S.addNode(20)
root.left.left = S.addNode(8)
root.left.right = S.addNode(12)
root.right.left = S.addNode(16)
root.right.right = S.addNode(25)
S.preOrder(root)
print "\n"
S.inOrder(root)
print "\n"
S.postOrder(root)