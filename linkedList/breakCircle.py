# http://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/

# Hash table
# https://www.youtube.com/watch?v=Aup0kOWoMVg

# Floyd's Cycle -- best algo O(N) time, no extra space
# https://www.youtube.com/watch?time_continue=452&v=apIw0Opq5nk
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None         

    def printNodes(self):
        curr = self
        while curr:
            print curr.data,
            curr = curr.next
        print ''

    def breakCircle(self):
        A = self
        flag = False
        mem = {A.data:[None]}
        while A and A.next:
            if A.next.data in mem:
                mem[A.next.data].extend([A])
                # break found duplicate:
                A.next = None
                flag = True
            else:
                mem[A.next.data] = [A]
            A = A.next    
        return flag

    def breakCircle2(self):
        head = slow = fast = self
        prevFast = None
        flag = False
        # detect if loop exists from second node
        while fast and fast.next and fast.next.next:
            slow = slow.next
            prevFast = fast
            fast = fast.next.next
            if slow.data == fast.data:
                flag = True
                break
        # if loop exists, locate the node before the loop
        # break the loop 
        if flag:
            slow = head
            prevFast = prevFast.next
            while slow != fast:
                slow = slow.next
                prevFast = fast
                fast = fast.next
            prevFast.next = None
        return flag



if __name__=='__main__':
    headA = Node(1)
    headA.next = Node(3)
    headA.next.next = Node(5)
    headA.next.next.next = Node(7)
    headA.next.next.next.next = Node(9)
    headA.next.next.next.next.next = Node(11)
    # make a circle Node(3)
    headA.next.next.next.next.next.next = headA.next.next
    # headA.printNodes()

    # print headA.breakCircle()
    # headA.printNodes()

    print headA.breakCircle2()
    headA.printNodes()
