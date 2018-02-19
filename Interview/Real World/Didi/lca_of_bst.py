def lca(root, p, q):
    if not root:
        return None
    if not p or not q:
        return root
    if root.val > p.val and root.val > q.val:
        return lca(root.right, p, q)
    elif root.val < p.val and root.val < q.val:
        return lca(root.left, p, q)
    else:
        return root

