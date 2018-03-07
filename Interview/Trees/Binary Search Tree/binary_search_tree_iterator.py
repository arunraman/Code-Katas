from binarytree import Node as Treenode

class Solution(object):

    def __init__(self, root):
        self.stack = list()
        self.pushAll(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.stack:
            return True
        return False

    # @return an integer, the next smallest number
    def next(self):
        tmpNode = self.stack.pop()
        self.pushAll(tmpNode.right)
        return tmpNode.value

    def pushAll(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left

root = Treenode(2)
root.left = Treenode(1)
root.left.left = Treenode(0)
root.right = Treenode(3)
print(root)

S = Solution(root)

print S.next()
print S.next()
print S.hasNext()
