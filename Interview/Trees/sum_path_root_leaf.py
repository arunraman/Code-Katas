from binarytree import Node as TN

class Solution(object):
    def roottoleafpathSum(self, root, s):
        if root == None:
            return s == 0
        else:
            ans = 0

            # Otherwise check both subtrees
            subSum = s - root.value

            # If we reach a leaf node and sum becomes 0, then
            # return True
            if (subSum == 0 and root.left == None and root.right == None):
                return True

            if root.left is not None:
                ans = ans or self.roottoleafpathSum(root.left, subSum)
            if root.right is not None:
                ans = ans or self.roottoleafpathSum(root.right, subSum)

            return ans


S = Solution()
s = 21
root = TN(10)
root.left = TN(8)
root.right = TN(2)
root.left.right = TN(5)
root.left.left = TN(3)
root.right.left = TN(2)
print(root)

print S.roottoleafpathSum(root, s)