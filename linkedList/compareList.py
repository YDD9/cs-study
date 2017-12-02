# http://www.geeksforgeeks.org/compare-two-strings-represented-as-linked-lists/
# https://stackoverflow.com/questions/227459/ascii-value-of-a-character-in-python
# ord('a') return 97 the ascii of 'a'
# chr(97) return 'a'
# unichr(97) return u'a'

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
        """
        keep removing the head and putting it into a new list as head
        return new list
        """
        result = LList()
        while self.head:
            result.insertHead(Node(self.head.data))
            self.removeHead()
        return result
        
    def compare(self, first, second):
        while first or second:
            fdata = sdata = None
            if first:
                fdata = first.data
                first = first.next
            if second:
                sdata = second.data
                second = second.next
            if fdata > sdata:
                return 1
            if fdata < sdata:
                return -1
        return 0

    def printLList(self):
        node = self.head
        while node:
            print node.data,
            node = node.next
        print '\n==============\n'

if __name__=='__main__':
    firstl = LList()
    secondl = LList()
    result = LList()

    firstl.insertHead(Node('B'))
    firstl.insertHead(Node('o'))
    firstl.insertHead(Node('x'))
    firstl.insertHead(Node('x'))
    firstl.printLList()

    secondl.insertHead(Node('b'))
    secondl.insertHead(Node('B'))
    secondl.insertHead(Node('o'))
    secondl.insertHead(Node('x'))
    secondl.insertHead(Node('x'))
    secondl.printLList()

    print result.compare(firstl.head, secondl.head), '\n========='