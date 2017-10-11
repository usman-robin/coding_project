from tree import BinarySearchTree

"""
/*
 Given a tree and a sum, return true if there is a path from the root
 down to a leaf, such that adding up all the values along the path
 equals the given sum.
 Strategy: subtract the node value from the sum when recurring down,
 and check to see if the sum is 0 when you run out of tree.
*/

1. We want to traverse all the nodes, so node.left and node.right must be called parallelly
2. One valid path is enough, so we want to use or to connect two "branches"
3. Considering each node as the root of its children, sum should be modified from its parent
"""


def hasPathSumRecursive(root, sum):
    if root is None:
        return False

    if root.left is None and root.right is None:
        return root.value == sum

    sum -= root.value

    return hasPathSumRecursive(root.left, sum) or hasPathSumRecursive(root.right, sum)


def hasPathSumIterative():
    pass

if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.add(15)
    tree.add(8)
    tree.add(18)
    tree.add(13)
    tree.add(7)
    tree.add(20)
    tree.add(22)
    print(hasPathSumRecursive(tree.root, 50))

"""
Questions for Shivraj:
Binary tree lookup/search using inorder? What does use mean DFS pathSum
Binary tree lookup/search using level order traversal
hasPathSum iterative(not needed)
isBST inorder traversal will print a sorted list
least common ancestor
loggin system
"""
