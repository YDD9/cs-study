# https://stackoverflow.com/a/28864021/5018506
class Node():
    def __init__(self, data):
        self.v = data
        self.l = None
        self.r = None

    def __str__(self):
        return data

class BT():
    def __init__(self):
        self.root = None

    def add(self, v):
        if self.root is None:
            self.root = Node(v)
        else:
            self._add(v, self.root)

    def _add(self, v, node):
        if v < node.v:
            if node.l is None:
                node.l = Node(v)
            else:
                self._add(v, node.l)
        else:
            if node.r is None:
                node.r = Node(v)
            else:
                self._add(v, node.r)


    def printTree(self):
        if self.root is None:
            print ''
        else:
            self._print(self.root)

    def _print(self, node):
        if node is not None:
            self._print(node.l)
            print str(node.v) + ' '
            self._print(node.r)


if __name__ == '__main__':
    btree = BT()
    btree.printTree()

    btree.add(3)
    btree.printTree()

    btree.add(2)
    btree.add(9)
    btree.printTree()

    btree.add(1)
    btree.add(4)
    btree.add(6)
    btree.printTree()