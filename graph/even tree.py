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


def nb_nodes(t, node, nb=[0]):
    """
    The problem here is that you need the same value to be shared by all of the recursive calls,
    which means you need a mutable value. So, you can start with [0] instead of 0,
    and do count[0] += 1 instead of count += 1.
    nb: list of two values, total nb of nodes including node itself
    """
    nb[0] += 1
    for subnode in t.get(node, ''):
        nb_nodes(t, subnode, nb)
    return nb


def nb_dfs(t, node):
    stack =[node]
    visited = []
    nb = 0
    while stack:
        cur = stack.pop()
        nb += 1
        if node in t and node not in visited:
            stack.extend(t[node])
        visited.append(cur)

    return nb


def cuts_even(t):
    cnt = 0
    # any non-leave node has the possibility to be cutted out
    for node in t:
        if nb_nodes(t, node)[0] % 2 == 0:
            cnt += 1
    return cnt-1 # the total tree is even and that cut is ingored


def cuts_even2(t):
    cnt = 0
    # any non-leave node has the possibility to be cutted out
    for node in t:
        if nb_dfs(t, node) % 2 == 0:
            cnt += 1
    return cnt-1 # the total tree is even and that cut is ingored

if __name__=='__main__':
    tree_from = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    tree_to = [1, 1, 3, 2, 1, 2, 6, 8, 8]
    # t={8: [9, 10], 1: [2, 3, 6], 2: [5, 7], 3: [4], 6: [8]}
    mytree=build_tree(tree_from, tree_to)
    print(mytree)

    print(cuts_even(mytree))

    t={8: [9, 10], 1: [2, 3, 6], 2: [5, 7], 3: [4], 6: [8], 4: [11, 12]}
    print(nb_dfs(t, 1))
    print(cuts_even2(t))
