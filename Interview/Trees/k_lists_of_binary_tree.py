from collections import deque

class Treenode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):

    def addNode(self, val):
        return Treenode(val)

    def k_list_of_lists_btree(self, root, k):
    	if root is None:
            return

        levelOrderqueue = deque()
        levelOrderqueue.append(root)
        result = []
        while True:
        	nodecount = len(levelOrderqueue)
        	if nodecount == 0 or k == 0:
        		break
        	temp_result = []
        	while nodecount > 0:
        		node = levelOrderqueue.popleft()
        		temp_result.append(node.val)
        		if node.left:
        			levelOrderqueue.append(node.left)
        		if node.right:
        			levelOrderqueue.append(node.right)
        		nodecount -= 1
        	result.append(temp_result)
        	k -= 1
        return result

S = Solution()
root = S.addNode(1)
root.left = S.addNode(2)
root.right = S.addNode(3)
root.left.left = S.addNode(4)
root.left.right = S.addNode(5)
root.right.left = S.addNode(6)
root.right.right = S.addNode(7)
print S.k_list_of_lists_btree(root, 2)