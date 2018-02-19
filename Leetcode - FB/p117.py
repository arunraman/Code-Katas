from TreeLinkNode import TreeLinkNode

class p117(object):

    def addNode(self, val):
        return TreeLinkNode(val)

    def connect(self, root):
        while root:
            cur = tmp = TreeLinkNode(0)
            while root:
                if root.left:
                    cur.next = root.left
                    cur = root.left
                if root.right:
                    cur.next = root.right
                    cur = root.right
                root = root.next
            root = tmp.next


S = p117()
root = S.addNode(3)
root.left = S.addNode(9)
root.right = S.addNode(20)
root.right.left = S.addNode(15)
root.right.right = S.addNode(7)
S.connect(root)