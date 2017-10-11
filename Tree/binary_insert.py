from tree import BinarySearchTree
from node import Node

## Insert to a node


def binary_insert(root, value):
    if root is None:
        root = Node(value)
    else:
        if root.value > value:
            if root.left is None:
                root.left = Node(value)
            else:
                binary_insert(root.left, value)
        else:
            if root.right is None:
                root.right = Node(value)
            else:
                binary_insert(root.right, value)




tree = BinarySearchTree()
tree.add(15)
tree.add(8)
tree.add(18)
tree.add(13)
tree.add(7)
tree.add(20)
tree.add(22)
