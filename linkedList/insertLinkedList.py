# http://www.geeksforgeeks.org/given-a-linked-list-which-is-sorted-how-will-you-insert-in-sorted-way/
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LList():
    def __init__(self):
        self.head = None

    def sortedInsert(self, newNode):
        if self.head is None:
            newNode.next = self.head
            self.head = newNode
        elif self.head.data >= newNode.data:
            newNode.next = self.head
            self.head = newNode
        else:
            current = self.head
            while(current.next is not None and current.next.data < newNode.data):
                current = current.next
            # 1 3 5 6
            # current 3, insert new node 5, current next 6
            newNode.next = current.next
            current.next = newNode

    def printList(self):
        current = self.head
        while(current):
            print current.data,
            current = current.next


if __name__ == '__main__':

    aLList = LList()

    A = Node(3)
    aLList.sortedInsert(A)
    # aLList.printList()

    B = Node(5)
    aLList.sortedInsert(B)
    # aLList.printList()

    C = Node(9)
    aLList.sortedInsert(C)
    # aLList.printList()

    x = Node(6)
    aLList.sortedInsert(x)
    aLList.printList()