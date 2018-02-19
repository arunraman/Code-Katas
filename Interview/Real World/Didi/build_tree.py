# give node and one of its child, build a tree, suppose no DAG

class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.children = list()

def build_tree(pairs):
    node_map = dict()
    parent_map = dict()
    child_map = dict()
    for pair in pairs:
        parent = None
        child = None
        if pair[0] not in node_map:
            parent = TreeNode(pair[0])
            node_map[pair[0]] = None
        else:
            parent = node_map[pair[0]]
        if pair[1] not in node_map:
            child = TreeNode(pair[1])
            node_map[pair[1]] = child
        else:
            child = node_map[pair[1]]
        parent.children.append(child)
        parent_map[pair[0]] = parent
        child_map[pair[1]] = child
    root = None
    for val in parent_map:
        if val not in child_map:
            root = parent_map[val]
            break
    return root

def dfs(root):
    if not root:
        return
    print root.val
    for child in root.children:
        dfs(child)

test = [('a', 'b'), ('a', 'c'), ('b', 'd')]
node = build_tree(test)
dfs(node)