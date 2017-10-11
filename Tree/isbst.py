from tree import BinarySearchTree
from node import Node
import sys

MAX_INT = sys.maxint
MIN_INT = -MAX_INT - 1

print(MAX_INT)
print (MIN_INT)


def isBST(node):
    return isBSTUtil(node, MIN_INT, MAX_INT)


def isBSTUtil(node, minval, maxval):

    # An empty tree is BST
    if node is None:
        return True

    # False if this node violates min/max constraint
    if node.data < minval or node.data > maxval:
        return False

    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (isBSTUtil(node.left, minval, node.data) and
            isBSTUtil(node.right, node.data, maxval))


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.add(15)
    tree.add(8)
    tree.add(18)
    tree.add(32)
    tree.add(4)
    tree.print_inorder()
    print(isBST(tree.root))


    tree.root.left.value = 27
    print("##################")
    print(tree.root.left.value)
    print("##################")

    tree.print_inorder()
    print(isBST(tree.root))

    #tree.add(13)
    #tree.add(7)
    #tree.add(20)
    #tree.add(22)



"""
Questions for Shivraj:
Binary tree lookup/search using inorder? What does use mean DFS pathSum
Binary tree lookup/search using level order traversal
hasPathSum iterative(not needed)
isBST inorder traversal will print a sorted list
least common ancestor
loggin system
"""
