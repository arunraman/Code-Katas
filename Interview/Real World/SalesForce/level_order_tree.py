from collections import deque

class Node(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class Solution(object):
    def addNode(self, data):
        return Node(data)

    def sumatLevel(self, root):
        if root is None:
            return

        levelOrderqueue = deque()
        levelOrderqueue.append(root)
        sumatLevel = 0
        while True:
            nodecount = len(levelOrderqueue)
            if nodecount == 0:
                break
            while (nodecount > 0):
                node = levelOrderqueue.popleft()
                sumatLevel += node.value
                if node.left:
                    levelOrderqueue.append(node.left)
                if node.right:
                    levelOrderqueue.append(node.right)
                nodecount -= 1
            print sumatLevel
            sumatLevel = 0



S = Solution()
root = S.addNode(1)
root.left = S.addNode(2)
root.right = S.addNode(3)
root.left.left = S.addNode(4)
root.left.right = S.addNode(5)
root.right.left = S.addNode(6)
root.right.right = S.addNode(7)
S.sumatLevel(root)