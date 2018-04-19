# Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# recursion
def maxDepth(self, root):
    if not root:
        return 0
    return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

# iterative
def maxDepth2(self, root):
    if not root:
        return 0

    tstack,h = [root],0

    #count number of levels
    while tstack:
        # process all nodes at same level
        nextlevel = []
        while tstack:
            top = tstack.pop()
            if top.left:
                nextlevel.append(top.left)
            if top.right:
                nextlevel.append(top.right)
        # only next level nodes passed to stack
        tstack = nextlevel
        # level count plus 1
        h+=1
    return h


def maxDepth3(self, root):
    maxDepth, stack = 0, [(root, 1)]
    while stack:
        node, level = stack.pop()
        # ignore None nodes at all levels
        if node:
            # update maxDepth
            maxDepth = max(maxDepth, level)
            # push left and right child onto stack
            stack.append((node.left, level+1))
            stack.append((node.right, level+1))
    return maxDepth