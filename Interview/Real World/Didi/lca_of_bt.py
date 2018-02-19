def lca(root, p, q):
    if root is None or root == p or root == q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root
    elif left:
        return left
    elif right:
        return right