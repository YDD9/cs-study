# http://www.geeksforgeeks.org/insertion-sort-for-singly-linked-list/

from insertLinkedList import Node, LList

def insertSortLList2(head):
    """
    To sort a given LList using insert sort algo.
    create a new empty LList, each time take one node from head and insert it into the LList.
    """
    result = Node(0)
    result.data = head.data
    result.next = None

    resultLList = LList()
    LList.head = result
    while head:
        newNode = Node(0)
        newNode.data = head.data
        newNode.next = None
        resultLList.sortedInsert(newNode)
        head = head.next
    resultLList.printList()
    return resultLList.head

head = Node(4)
head.next = Node(1)
head.next.next = Node(3)
head.next.next.next = Node(2)
insertSortLList2(head)
