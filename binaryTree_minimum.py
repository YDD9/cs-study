# Python program to find minimum depth of a given Binary Tree
 
# Tree node
class Node:
    def __init__(self , key):
        self.data = key 
        self.left = None
        self.right = None
 
def minDepth(root):
    # Corner Case.Should never be hit unless the code is 
    # called on root = NULL
    if not root:
        return 0
    elif not root.left or not root.right:
        return minDepth(root.left) + minDepth(root.right) + 1
    else:
        return min(minDepth(root.left), minDepth(root.right)) + 1

# Driver Program 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print minDepth(root)

sum([[1,2], [0], [56,6]], [])

# http://www.geeksforgeeks.org/find-minimum-depth-of-a-binary-tree/