# http://www.geeksforgeeks.org/select-a-random-node-from-a-singly-linked-list/
# https://leetcode.com/problems/linked-list-random-node/discuss/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        

    def getRandom(self):
        import random
        """
        Returns a random node's value.
        :rtype: int
        """
        reservoirHead = self.head
        node = self.head.next
        count = 1
        while node:
            j = random.randrange(count)  
            # np.random.randint(1) https://www.mathworks.com/help/matlab/math/floating-point-numbers-within-specific-range.html
            if j < 1:
                reservoirHead = node
            count += 1
            node = node.next
        return reservoirHead.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

