from tree import BinarySearchTree

# In binary search tree


def searchRecursive(node, val):
    if node is None:
        return False
    if node.value == val:
        return True
    else:
        if node.value > val:
            return searchRecursive(node.left, val)
        else:
            return searchRecursive(node.right, val)




# we will use the level order traversal

"""
Create a queue.
Push root into the queue.
Loop
	nodeCount = size of queue

    // If number of nodes at this level is 0, return height
	if nodeCount is 0
		return Height;
	else
		increase Height

        // Remove nodes of this level and add nodes of
        // next level
	while (nodeCount > 0)
		pop node from front
		push its children to queue
		decrease nodeCount
       // At this point, queue has nodes of next level
"""
def searchLevelOrder(root, val):
    if root is None:
        return False
    q = []
    q.append(root)

    while len(q) > 0:
        node = q.pop(0)
        if node.value == val:
            return True
        else:
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
    return False


def searchInorder(node, val):
    """
    1) Create an empty stack S.
    2) Initialize current node as root
    3) Push the current node to S and set current = current->left until current is NULL
    4) If current is NULL and stack is not empty then
        a) Pop the top item from stack.
        b) Check if the value is equal to node.value return true
        c) Go to step 3.
    5) If current is NULL and stack is empty then we are done.
    """
    cur = node
    stack = []
    done = 0
    while not done:
        # Insert all the left values
        while cur is not None:
            stack.append(cur)
            cur = cur.left

        if stack:
            popped = stack.pop()
            if popped.value == val:
                return True
            cur = popped.right

        if cur is None and not stack:
            done = 1

    return False


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.add(15)
    tree.add(8)
    tree.add(18)
    tree.add(13)
    tree.add(7)
    tree.add(20)
    tree.add(22)
    tree.add(19)
    #tree.print_inorder()
    #print(searchRecursive(tree.root, 20))
    #print(searchRecursive(tree.root, 30))
    #print(searchLevelOrder(tree.root, 20))
    #print(searchLevelOrder(tree.root, 30))
    print(searchInorder(tree.root, 20))
    print(searchInorder(tree.root, 30))