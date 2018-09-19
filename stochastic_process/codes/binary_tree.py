class Node:
    def __init__(self, item, leaf):
        self.child1 = None
        self.child2 = None
        self.item = item
        self.leaf = leaf

    def addChild(self, c1, c2):
        self.child1 = c1
        self.child2 = c2

    def isLeaf(self):
        return self.leaf
    
def traverse(node, code, slist):
    if node.isLeaf():
        # print node.item.letter, node.item.prob, code
        node.item.code = code
        slist[ord(node.item.letter)-97] = node.item
    else:
        traverse(node.child1,code+'0',slist)
        traverse(node.child2,code+'1',slist)


def main():
    n1 = Node('a', False)

    n21 = Node('b', False)
    n22 = Node('c', False)

    n1.addChild(n21, n22)

    n31 = Node('d',True)
    n32 = Node('e',True)
    n33 = Node('f',True)
    n34 = Node('g',True)

    n21.addChild(n31, n32)
    n22.addChild(n33, n34)

    # traverse
    traverse(n1)



if __name__ == '__main__':
    main()

