# https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        def level(root, lev=0):
            lev = lev
            if root is None or (root.left is None and root.right is None):
                return lev
            lev += 1
            lev = max(level(root.left, lev), level(root.right, lev))
            return lev

        r = 1 if root.right else 0
        l = 1 if root.left else 0
        return abs(level(root.right, r) - level(root.left, l)) <= 1 and\
                self.isBalanced(root.left) and self.isBalanced(root.right)

# https://leetcode.com/problems/balanced-binary-tree/discuss/35809/Python-ITERATIVE-solution
class Solution2(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = [root]
        visited = []
        lev = 0
        while stack:
            cur = stack.pop()
            lev += 1
            if cur.left not in stack and cur.left not in visited:
                stack.append(cur.left)
            if cur.right not in stack and cur.right not in visited:
                stack.append(cur.right)
            visited.append(cur)


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def main():
    # import sys
    # def readlines():
    #     for line in sys.stdin:
    #         yield line.strip('\n')
    # lines = readlines()
    # while True:
    #     try:
    #         line = lines.next()
    # root = stringToTreeNode('[1,null,2,null,3]')
    # root = stringToTreeNode('[1,2,2,3,null,null,3,4,null,null,4]')
    root = stringToTreeNode('[3,9,20,null,null,15,7]')

    ret = Solution().isBalanced(root)

    out = (ret)
    print out
        # except StopIteration:
        #     break

if __name__ == '__main__':
    main()