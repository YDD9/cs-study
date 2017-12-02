class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class linkedl(object):
    def __init__(self):
        self.head = None

    def push(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode      

    def addTwol(self, first, second):
        resl = linkedl()
        carry = 0
        root = n = Node(0)
        while first or second:
            # get node value if exist, otherwise 0
            fval = 0 if first is None else first.val
            sval = 0 if second is None else second.val
            val = (carry + fval + sval) % 10
            carry = (fval + sval) // 10
            # move to next bit if exist
            first = None if first is None else first.next
            second = None if second is None else second.next

            temp = Node(val)
            # assign the head
            if self.head is None:
                self.head = temp
            else:
                # next is temp
                previous.next = temp
            # move previous forward    
            previous = temp

            n.next = Node(val)
            n = n.next
            print 'root.val %r,\troot.next %r' % (root.val, root.next.val)
            print 'n.val %r,\tn.next: %r\n' % (n.val, n.next)

            resl.push(val)
        # add last carry to next node if carry exist
        if carry:
            resl.push(carry)

        return resl

    def printLinkedl(self):
        node = self.head
        while node:
            print node.val,
            node = node.next
        print ''


if __name__=='__main__':
    list1 = linkedl()
    list2 = linkedl()
    res = linkedl()

    list1.push(0)
    list1.push(2)
    list1.push(5)
    list1.printLinkedl()

    list2.push(5)
    list2.push(1)
    list2.push(9)
    list2.push(3)
    list2.printLinkedl()

    result = res.addTwol(list1.head, list2.head)
    # with the returned linked list, order is wrong
    result.printLinkedl()
    
    # with the implicit list without return, order is correct
    res.printLinkedl()





# most clean solution
# https://leetcode.com/problems/add-two-numbers/discuss/
# https://discuss.leetcode.com/topic/8909/clear-python-code-straight-forward

# easier to understand solution
# http://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-lists/        