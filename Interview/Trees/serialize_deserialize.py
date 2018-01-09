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

    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')

        vals = []
        doit(root)
        return ' '.join(vals)


    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = Treenode(int(val))
            node.left = doit()
            node.right = doit()
            return node

        vals = iter(data.split())
        return doit()

S = Solution()
root = S.addNode(1)
root.left = S.addNode(2)
root.right = S.addNode(3)


print S.serialize(root)
print S.deserialize('1 2 # # 3 # #').val