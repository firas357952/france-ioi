tree = [3, 3, 7, 3, 6, 7, 0, 0]

def children(tree):
    child = {}
    for idx, n in enumerate(tree):
        try:
            child[n].append(idx + 1)
        except Exception:
            child[n] = []
            child[n].append(idx + 1)
    return child

tree = children(tree)

def node_children(node, tree):
    try:
        children = tree[node]
        return children
    except Exception:
        return []


def bfs(node, tree):
    L = [node]
    Q = [node]
    while Q != []:
        N = node_children(Q[0], tree)
        Q.pop(0)
        Q.extend(N)
        L.extend(N)
    return L


result = bfs(0, tree)
print(result)
