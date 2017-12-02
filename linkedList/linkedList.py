# https://www.pythoncentral.io/reverse-singly-linked-list/
# https://www.teamten.com/lawrence/writings/reverse_a_linked_list.html

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LList(object):
    def __init__(self):
        self.head = None

    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        prev.next = newNode

    def insertHead(self, newNode):
        newNode.next = self.head
        self.head = newNode

    def removeAfter(self, prev):
        prev.next = prev.next.next
        # prev.next.next = None # not correct this line

    def removeHead(self):
        self.head = self.head.next
        # self.head.next = None # not correct this line

    def reverseLList(self):
        prev = None
        curr = self.head
        nex = curr.next
        while curr:
            curr.next = prev
            prev = curr
            curr = nex
            nex = nex.next if nex else None    
        self.head = prev          

    def reverseLList2(self, node):
        if node.next is None:
            self.head = node
            return
        self.reverseLList2(node.next)
        # below link reverse operation will be recursively executed as well, and it runs at each node 
        # when head is found, each recursive step will go one node back and execute below code for that node.
        # when writing the below code, think only the case of last recursive step(a step has no more recursive):
        # reversing link between head and head.next
        temp = node.next
        temp.next = node
        node.next = None

    def reverseLList3(self):
        result = LList()
        while self.head:
            result.insertHead(Node(self.head.data))
            self.removeHead()
        return result
        
    def printLList(self):
        node = self.head
        while node:
            print node.data,
            node = node.next
        print '\n==============\n'

if __name__=='__main__':
    linkList = LList()
    n5 = Node(5)
    n1 = Node(1)
    n10 = Node(10)
    n15 = Node(15)
    n11 = Node(11)

    print 'Prepare orig linked list via insert head and after:'
    linkList.insertHead(n5)
    linkList.insertHead(n1)
    linkList.insertAfter(n5, n10)
    # only for understand recursive inside reverseLList2
    # linkList.reverseLList2(n1)
    # linkList.printLList()
    linkList.insertAfter(n10, n15)
    linkList.insertAfter(n10, n11)
    linkList.printLList()
    
    print 'Testing remove head:'
    linkList.removeHead()
    linkList.printLList()
    linkList.removeHead()
    linkList.printLList()

    print 'Preparing orig linked list via insert head and after:'
    linkList.insertHead(n1)
    linkList.printLList()
    linkList.insertAfter(n1, n5)
    linkList.printLList()

    print 'Testing remove after:'
    linkList.removeAfter(n5)
    linkList.printLList()
    linkList.removeAfter(n1)
    linkList.printLList()

    print 'Testing reverse linked list:'
    linkList.insertAfter(n1, n5)
    linkList.insertAfter(n5, n10)
    linkList.printLList()
    linkList.reverseLList()
    linkList.printLList()
    linkList.reverseLList2(n15)
    linkList.printLList()
    
    reversedLList = linkList.reverseLList3()
    reversedLList.printLList()