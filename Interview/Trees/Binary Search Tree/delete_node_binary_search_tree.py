from binarytree import Node as Treenode

class Solution(object):
    def insert(self, node, value):
        if node is None:
            return Treenode(value)

        if value < node.value:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)

        return node

    def get_minimum_value_node(self, root):
        currNode = root
        while currNode.left is not None:
            currNode = currNode.left
        return currNode

    def inorder_traversal(self, root):
        if root is not None:
            self.inorder_traversal(root.left)
            print root.value,
            self.inorder_traversal(root.right)

    def delete_node(self, root, value):
        # Base Case
        if root is None:
            return root

            # If the key to be deleted is smaller than the root's
        # key then it lies in  left subtree
        if value < root.value:
            root.left = self.delete_node(root.left, value)

        # If the kye to be delete is greater than the root's key
        # then it lies in right subtree
        elif (value > root.value):
            root.right = self.delete_node(root.right, value)

        # If key is same as root's key, then this is the node
        # to be deleted
        else:

            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children: Get the inorder successor
            # (smallest in the right subtree)
            temp = self.get_minimum_value_node(root.right)

            # Copy the inorder successor's content to this node
            root.value = temp.value

            # Delete the inorder successor
            root.right = self.delete_node(root.right, temp.value)

        return root


S = Solution()
root = None
root = S.insert(root, 50)
root = S.insert(root, 30)
root = S.insert(root, 20)
root = S.insert(root, 40)
root = S.insert(root, 70)
root = S.insert(root, 60)
root = S.insert(root, 80)
print root
S.inorder_traversal(root)
root = S.delete_node(root, 20)
print root