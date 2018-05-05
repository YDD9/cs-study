# https://www.geeksforgeeks.org/convert-tree-forest-even-nodes/
# https://www.hackerrank.com/challenges/even-tree/problem

def build_tree(t_from, t_to):
    """
    build adj-list of the tree
    https://docs.python.org/2/library/collections.html#defaultdict-examples

    >>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    >>> d = defaultdict(list)
    >>> for k, v in s:
    ...     d[k].append(v)
    ...
    >>> d.items()
    [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
    """
    t_ = {}
    for index, item in enumerate(t_to):
        if item not in t_:
            t_[item] = [tree_from[index]]
        else:
            t_[item].append(tree_from[index])
    return t_

# recursive method 1
def nb_nodes(t, node, nb=[0]):
    """
    The problem here is that you need the same value to be shared by all of the recursive calls,
    which means you need a mutable value. So, you can start with [0] instead of 0,
    and do count[0] += 1 instead of count += 1.
    nb: list of two values, total nb of nodes including node itself
    """
    if not node:
        return nb[0]
    nb[0] += 1
    for subnode in t.get(node, ''):
        nb_nodes(t, subnode, nb)
    return nb[0]

def cuts_even(t, root, n=[0]):
    if not root: return n[0]
    # each node start from [0] to count, otherwise it starts for n of their parents
    if nb_nodes(t, root, [0]) % 2 == 0:
        n[0] += 1
    # any non-leave node has the possibility to be cutted out
    for subnode in t.get(root, ''):
        cuts_even(t, subnode, n)
    return n[0] # the total tree is even and that cut is ingored

# stack method 2
def nb_nodes2(t, node):
    stack =[node]
    nb = 0
    tmp = t.copy()
    while stack:
        cur = stack.pop()
        nb += 1
        if cur in tmp:
            stack.extend(tmp.pop(cur))
    return nb

def cuts_even2(t, root):
    stack = [root]
    cut = 0
    tmp = t.copy()
    while stack:
        cur = stack.pop()
        if nb_nodes2(tmp, cur) % 2 == 0:
            cut += 1
        if cur in tmp:
            stack.extend(tmp.pop(cur))
    return cut-1



if __name__=='__main__':
    tree_from = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    tree_to = [1, 1, 3, 2, 1, 2, 6, 8, 8]
    # t={8: [9, 10], 1: [2, 3, 6], 2: [5, 7], 3: [4], 6: [8]}
    mytree=build_tree(tree_from, tree_to)
    print(mytree)
    print(nb_nodes(mytree, 9, [0]))
    print(nb_nodes(mytree, 5, [0]))
    print(nb_nodes(mytree, 4, [0]))
    print(nb_nodes(mytree, 6, [0]))
    print(nb_nodes(mytree, 1, [0]))
    print(cuts_even(mytree, 1) - 1)

    # methode 2
    t={8: [9, 10], 1: [2, 3, 6], 2: [5, 7], 3: [4], 6: [8]}
    print(nb_nodes2(t, 2))
    print(cuts_even2(t, 1))
