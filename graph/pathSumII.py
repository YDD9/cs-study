# https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import defaultdict

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # recursive DFS
        # def curSum(node, target):
        #     if node is None:
        #         return False
        #     if node.left is None and node.right is None:
        #         return node.val == target
        #     # if node.left: won't return
        #     #     return curSum(node.left, target-node.val)
        #     # if node.right:
        #     return curSum(node.right, target-node.val) or curSum(node.left, target-node.val)

        # return curSum(root, sum)


        if root is None:
            return []

        stack, res, meta = [(root, sum)],[],{root:None}

        while stack:
            node, target = stack.pop()

            if node.left is None and node.right is None:
                if node.val==target:
                    res.append(node)

            target -= node.val
            if node.right:
                stack.append((node.right, target))
                meta[node.right] = node
            if node.left:
                stack.append((node.left, target))
                meta[node.left] = node

        def construct_Path(res, meta):
            paths = []
            for leaf in res:
                path = [leaf.val]
                while leaf is not None and meta[leaf]:
                    path.append(meta[leaf].val)
                    leaf = meta[leaf]
                paths.append(path[::-1])
            return paths

        return construct_Path(res, meta)



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

def stringToInt(input):
    return int(input)

def main():
    # import sys
    # def readlines():
    #     for line in sys.stdin:
    #         yield line.strip('\n')
    # lines = readlines()
    # while True:
    #     try:
    #         line = lines.next()
    #         root = stringToTreeNode(line)
    root = stringToTreeNode('[5,4,8,11,null,13,4,7,2,null,null,null,1]')
    #         line = lines.next()
    #         sum = stringToInt(line)
    sum = 22

    ret = Solution().pathSum(root, sum)

    out = (ret)
    print out
    #     except StopIteration:
    #         break

if __name__ == '__main__':
    main()