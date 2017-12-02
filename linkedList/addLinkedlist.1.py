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
        carry = 0
        temp = Node(0)
        while first or second or carry:
            fval = sval = 0
            if first:
                fval = first.val
                first = first.next
            if second:
                sval = second.val
                second = second.next
            carry, remainder = divmod(fval+sval+carry, 10)
            temp.next = Node(remainder)
            if self.head is None:
                self.head = temp.next
            temp = temp.next

        return self.head

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

    list1.push(9)
    list1.push(2)
    list1.push(5)
    list1.printLinkedl()

    list2.push(9)
    list2.push(5)
    list2.push(9)
    list2.push(3)
    list2.printLinkedl()

    res.addTwol(list1.head, list2.head)
    res.printLinkedl()


# most clean solution
# https://leetcode.com/problems/add-two-numbers/discuss/
# https://discuss.leetcode.com/topic/8909/clear-python-code-straight-forward

# easier to understand solution
# http://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-lists/        