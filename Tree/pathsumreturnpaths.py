from tree import BinarySearchTree

"""
/*

"""


def hasPathSumpaths(root, sum):
    results = []

    pathhelper(root, sum, results, [])

    return results


def pathhelper(root, sum, results, path):

    if root is None:
        return []

    if root.left is None and root.right is None and root.value == sum:
        path.append(root.value)
        results.append(path)

    sum -= root.value

    pathhelper(root.left, sum, results, path + [root.value])
    pathhelper(root.right, sum, results, path + [root.value])

if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.add(8)

    tree.add(12)
    tree.add(7)
    tree.add(5)
    print(hasPathSumpaths(tree.root, 20))

"""
Questions for Shivraj:
Binary tree lookup/search using inorder? What does use mean DFS pathSum
Binary tree lookup/search using level order traversal
hasPathSum iterative(not needed)
isBST inorder traversal will print a sorted list
least common ancestor
loggin system
"""
