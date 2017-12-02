class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def printNode(self):
        print self.data, '--->', self.next.data

class LList(object):
    def __init__(self):
        self.head = None

    def pushHead(self):
        pass

    def printLList(self):
        node = self.head
        while node:
            print node.data,
            node = node.next
        print ''

    @staticmethod  # make this just as a pure function
    def getMedianNode(head):
        slow = fast = head # keep moving fast pointer at 2x speed of slow
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    @staticmethod  # make this just as a pure function
    def mergeLList(n1, n2):
        tmp = start = Node(0)
        while n1 and n2:
            if n1.data <= n2.data:
                start.next = n1
                n1 = n1.next
            else:
                start.next = n2
                n2 = n2.next
            start = start.next
        if n1 or n2:
            start.next = n1 or n2
        return tmp.next

    @staticmethod  # make this just as a pure function
    def mergeSortLList(headNode):
        if headNode and headNode.next: 
            n1 = headNode
            medianNode = LList.getMedianNode(headNode)
            n2 = medianNode.next
            medianNode.next = None
            return LList.mergeLList(LList.mergeSortLList(n1), LList.mergeSortLList(n2))
        # quit when headNode is single node, no splitting anymore
        return headNode

head = Node(4)
head.next = Node(2)
head.next.next = Node(3)
head.printNode()

lList = LList()
lList.head = head
lList.printLList()

newHead = LList.mergeSortLList(head)
newHead.printNode()
newlList = LList()
newlList.head = newHead
newlList.printLList()

# explain @classmethod and @staticmethod
# https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner