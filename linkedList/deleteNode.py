# http://www.geeksforgeeks.org/delete-a-given-node-in-linked-list-under-given-constraints/
# https://stackoverflow.com/questions/13090896/cant-remove-first-node-in-linked-list

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    def printNodes(self):
        tmp = self
        while tmp:
            print tmp.data,
            tmp = tmp.next


def deleteNode(node, dNode):
    if node.data == dNode.data:
        if node.next:
            # update value of node
            node.data = node.next.data
            # let updated node link to the next of the next
            node.next = node.next.next
            return 
        else:
            # Only node in list
            node.data = None
            node.next = None
            return 
    while node.next:
        if node.next.data == dNode.data:
            node.next = node.next.next
            return
        node = node.next
    # dNode not found
    return -1


if __name__=='__main__':
    n1 = Node(1)
    n5 = Node(5)
    n10 = Node(10)
    n15 = Node(15)
    n50 = Node(50)
    n100 = Node(100)
    n1.next = n5
    n5.next = n10
    n10.next = n15
    n15.next = n50
    n50.next = n100

    # start from 2nd(as head)to delete last node
    deleteNode(n5, n100)
    n5.printNodes()
    print ''

    # delete head node
    deleteNode(n5, n5)
    n5.printNodes()
    print ''

    # delete no existing node
    deleteNode(n10, n100)
    n10.printNodes()
    print ''
   
    # delete a node in between
    deleteNode(n10, n15)
    n10.printNodes()
    print ''