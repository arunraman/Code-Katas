class Tree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):

    def isuniVal(self, root):
        isunivalornot_1, count_of_single_uni_val_subtree = self.isunivalRecu(root, count=0)
        isunivalornot_2, count_of_uni_val_subtree = self.isunivalRecu_1(root, count=0)
        return isunivalornot_1, count_of_single_uni_val_subtree, count_of_uni_val_subtree

    def isunivalRecu(self, root, count):
        if not root:
            return True , count

        left, count = self.isunivalRecu(root.left, count)
        right, count = self.isunivalRecu(root.right, count)

        if self.issameValue(root, root.left, left) and \
            self.issameValue(root, root.right, right):
            count += 1
            return True , count

        return False, count

    def isunivalRecu_1(self, root, count):
        if not root:
            return True , count

        left, count = self.isunivalRecu_1(root.left, count)
        right, count = self.isunivalRecu_1(root.right, count)

        if self.issameValue(root, root.left, left) and \
            self.issameValue(root, root.right, right):
            if root.left != None and root.right != None:
                count += 1
            return True , count

        return False, count

    def issameValue(self, root, child_node, isUni):
        return not child_node or (isUni and root.val == child_node.val)

T = Tree(1)
T.left = Tree(1)
T.right = Tree(1)
T.left.left = Tree(1)
T.left.right = Tree(1)
T.right.left = Tree(1)
T.right.right = Tree(1)

T1 = Tree(1)
T1.left = Tree(2)
T1.right = Tree(3)
T1.left.left = Tree(2)
T1.left.right = Tree(2)
T1.right.left = Tree(3)
T1.right.right = Tree(3)

S = Solution()
print S.isuniVal(T1)
print S.isuniVal(T)