import heapq

class Treenode():
    def __init__(self, x=None):
        self.value = x
        self.left = None
        self.right = None


class Solution():
    def __init__(self):
        self.maxSum = float("-inf")
        self.max_len = 0
        self.serial = []

    def addNode(self, data):
        return Treenode(data)

###########################################################################

    def binaryTreeToArray(self, root):
        if root is None:
            return []
        return self.binaryTreeToArray(root.left) + [root.value] + self.binaryTreeToArray(root.right)

###########################################################################

    def maxPathSum(self, root):
        self.maxPathSumRecurse(root)
        return self.maxSum

    def maxPathSumRecurse(self, root):
        if root is None:
            return 0
        left = max(0, self.maxPathSumRecurse(root.left))
        right = max(0, self.maxPathSumRecurse(root.right))
        self.maxSum = max(self.maxSum, root.value + left + right)
        return root.value + max(left, right)

###########################################################################

    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isSymmetricRecurse(root, root)

    def isSymmetricRecurse(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if(root1 is not None and root2 is not None):
            if root1.value == root2.value:
                return (self.isSymmetricRecurse(root1.left, root2.right) and
                        self.isSymmetricRecurse(root1.right, root2.left))

###########################################################################

    def longestConsecutiveRecurse(self, root):
        if not root:
            return 0
        left_len = self.longestConsecutiveRecurse(root.left)
        right_len = self.longestConsecutiveRecurse(root.right)

        cur_len = 1

        if (root.left and root.left.value == root.value + 1):
            cur_len = max(cur_len, left_len + 1)
        if (root.right and root.right.value == root.value + 1):
            cur_len = max(cur_len, right_len + 1)
        self.max_len = max(self.max_len, cur_len, left_len, right_len)

        return self.max_len

###########################################################################

    def maxHeight(self, root):
        if not root:
            return 0
        else:
            return max(self.maxHeight(root.left),
                       self.maxHeight(root.right)) + 1

    def isheightBalanced(self, root):
        if root == None:
            return True
        if self.maxHeight(root.left) - self.maxHeight(root.right) <= 1:
            return self.isheightBalanced(root.left) and self.isheightBalanced(root.right)
        else:
            return False

###########################################################################

    def serializeRecu(self, root):
        if not root:
            self.serial.append('#')
        else:
            self.serial.append(root.value)
            self.serializeRecu(root.left)
            self.serializeRecu(root.right)
        return ''.join(str(self.serial))

    def deSerializeRecu(self, data):
        # """Decodes your encoded data to tree.
        #
        # :type data: str
        # :rtype: TreeNode
        # """
        #

        # def deserializeHelper():
        #     val = next(vals)
        #     if val == '#':
        #         return None
        #     else:
        #         node = TreeNode(int(val))
        #         node.left = deserializeHelper()
        #         node.right = deserializeHelper()
        #         return node
        #
        # def isplit(source, sep):
        #     sepsize = len(sep)
        #     start = 0
        #     while True:
        #         idx = source.find(sep, start)
        #         if idx == -1:
        #             yield source[start:]
        #             return
        #         yield source[start:idx]
        #         start = idx + sepsize
        #
        # vals = iter(isplit(data, ' '))
        # return deserializeHelper()
        pass
    ###########################################################################

    def sortedArrayToBST(self, num):
        return self.sortedArrayToBSTRec(num, 0, len(num) - 1)

    def sortedArrayToBSTRec(self, num, begin, end):
        if begin > end:
            return None
        midPoint = (begin + end) // 2
        root = Treenode(num[midPoint])
        root.left = self.sortedArrayToBSTRec(num, begin, midPoint - 1)
        root.right = self.sortedArrayToBSTRec(num, midPoint + 1, end)
        return root

###############################################################################

    def countUnivalSubtrees(self, root):
        count = [0]
        self.checkUni(root, count)
        return count[0]

    def checkUni(self, root, count):
        if root is None:
            return True

        left = self.checkUni(root.left, count)
        right = self.checkUni(root.right, count)

        if left == False and right == False:
            return False

        if root.left and root.value != root.left.value:
            return False

        if root.right and root.value != root.right.value:
            return False

        count[0] += 1

        return True

    ###############################################################################

    def displayTree(self, root):
        thislevel = [root]
        while thislevel:
            nextlevel = list()
            for n in thislevel:
                print n.value,
                if n.left: nextlevel.append(n.left)
                if n.right: nextlevel.append(n.right)
            print
            thislevel = nextlevel


S = Solution()
root = S.addNode(1)
root.left = S.addNode(2)
root.right = S.addNode(3)
root.left.left = S.addNode(4)
root.left.right = S.addNode(5)
root.right.left = S.addNode(6)
root.right.right = S.addNode(7)

print "Maximum Path Sum : " + str(S.maxPathSum(root))

if S.isSymmetric(root):
    print "The Binary Tree is Symmetric"
else:
    print "The Binary Tree is Not Symmetric"

# To convert binary tree to BST
# push the array to heapq and construct BST
bst_array = S.binaryTreeToArray(root)
sorted_array = []
for i in bst_array:
    heapq.heappush(sorted_array, i)
bsTree = S.sortedArrayToBST(sorted_array)

# longest consecutive
print "Longest Consecutive Length " + str(S.longestConsecutiveRecurse(root))

# max height of BTree
print "Max height of binary tree " + str(S.maxHeight(root))

# Serial De-Serialize
string = S.serializeRecu(root)
print "Serialization : " + string

print "De-Serialization : " + str(S.deSerializeRecu(string))
# Height Balanced or not
if S.isheightBalanced(root):
    print "BTree is height balanced"
else:
    print "BTree is not height balanced"

print "Number of Univalue Subtrees : " + str(S.countUnivalSubtrees(root))

# Display the tree level order
S.displayTree(root)
# S.displayTree(bsTree)