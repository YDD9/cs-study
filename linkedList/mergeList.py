# http://www.geeksforgeeks.org/merge-a-linked-list-into-another-linked-list-at-alternate-positions/

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def merge(self, B):
        A = self
        while A and B:
            newheadB = B.next
            B.next = A.next
            A.next = B
            # new assignment for A, self and A no longer point to the same underlying object
            # But operation on this new A update element in self, which update self.next.next
            A = A.next.next  
            B = newheadB
        return newheadB

    def union(self, B):
        prev = None
        A = self
        mem = dict()
        intersection = []
        while A:
            mem[A.data] = True
            prev = A
            A = A.next
        while B:
            if B.data not in mem:
                prev.next = B
                prev = B
            else:
                print B.data,
                intersection.append(B.data)
            B = B.next
        print ''
        return intersection
                
    def union2(self, B):
        intersection = []
        flag = True
        headA = A = self
        while B:
            nextB = B.next
            while A:
                if B.data == A.data:
                    flag = False
                    intersection.append(B.data)
                    print B.data,
                    break
                A = A.next
            if flag:
                B.next = headA
                headA = B
            B = nextB
        print ''
        return intersection
                

    def printNodes(self):
        curr = self
        while curr:
            print curr.data,
            curr = curr.next
        print ''

    

if __name__=='__main__':
    headA = Node(1)
    headA.next = Node(3)
    headA.next.next = Node(5)
    headA.next.next.next = Node(7)
    headA.printNodes()

    headB = Node(2)
    headB.next = Node(4)
    headB.next.next = Node(6)
    headB.next.next.next = Node(8)
    headA.merge(headB)
    # headA.merge(headB).printNodes()
    headA.printNodes()

    headC = Node(4)
    headC.next = Node(8)
    headC.next.next = Node(9)
    headC.next.next.next = Node(10)
    # headA.union(headC)
    # headA.printNodes()
    headA.union2(headC)
    headA.printNodes()
