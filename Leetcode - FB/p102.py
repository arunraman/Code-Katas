from TreeNode import TreeNode
from collections import deque

class p102(object):

    def addNode(self, val):
        return TreeNode(val)

    def levelorderTraversal(self, root):
        if root is None:
            return []

        levelorderQueue = deque()
        levelorderQueue.append(root)
        result = []
        while True:
            nodeCount = len(levelorderQueue)
            tempResult = []
            if nodeCount == 0:
                break
            while nodeCount != 0:
                node = levelorderQueue.popleft()
                tempResult.append(node.val)
                if node.left:
                    levelorderQueue.append(node.left)
                if node.right:
                    levelorderQueue.append(node.right)
                nodeCount -= 1
            result.append(tempResult)
        return result




S = p102()
root = S.addNode(3)
root.left = S.addNode(9)
root.right = S.addNode(20)
root.right.left = S.addNode(15)
root.right.right = S.addNode(7)
print S.levelorderTraversal(root)