    # Definition for a binary tree node.
    class TreeNode(object):
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    from collections import defaultdict

    class Solution(object):
        def hasPathSum(self, root, sum):
            """
            :type root: TreeNode
            :type sum: int
            :rtype: bool
            """


            def curSum(node, target):
                if node is None:
                    return False
                if node.left is None and node.right is None and node.val == target:
                    return True
                if node.left:
                    return curSum(node.left, target-node.val)
                if node.right:
                    return curSum(node.right, target-node.val)

            return curSum(root, sum)

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
        root = stringToTreeNode('[5,4,8,11,null,13,4,7,2,null,null,null,1]')
        sum = 22

        ret = Solution().hasPathSum(root, sum)

        out = (ret)
        print out


    if __name__ == '__main__':
        main()