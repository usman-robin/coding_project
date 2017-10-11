from tree import BinarySearchTree
from tree import BinaryTree


class BTIterator(object):

    def __init__(self, root):
        self.root = root
        self.stack = []

        self._populate_lefts(root)

    def _populate_lefts(self, root):
        while root is not None:

            self.stack.append(root)
            root = root.left

    def print_stack(self):
        lst = []
        for i in self.stack:
            lst.append(i.value)
        return lst

    def next(self):
        #self.stack = []
        print("IN NEXT")
        if not self.has_next():
            raise Exception("Stack is empty")

        ret = self.stack.pop()
        n = ret.right

        #print(n.value)

        while n is not None:
            ## Append the right value
            self.stack.append(n)
            ## Check to see if there is a left value
            n = n.left

        print("Returning Value : {}".format(ret.value))
        print(self.print_stack())
        return ret.value

    def has_next(self):
        #return not len(self.stack)
        #return not len(self.stack) == 0
        if self.stack:
            return True
        else:
            return False

        #return len(self.stack) != 0



tree = BinarySearchTree()
tree.add(15)
tree.add(8)
tree.add(18)
tree.add(13)
tree.add(7)
#tree.add(19)
#tree.add(16)
#tree.add(12)
#tree.add(14)


#tree.add(1)
#tree.add(2)
#tree.add(5)
#tree.add(3)
#tree.add(6)
#tree.add(4)
#print tree.is_empty()
#tree.PrintTree()

#tree.print_inorder()

it = BTIterator(tree.root)
#print(it.print_stack())

while it.has_next():
    #it.next()
    print(it.next())
