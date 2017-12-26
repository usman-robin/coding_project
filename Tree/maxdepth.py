from tree import BinarySearchTree


def maxDepth(node):
    if node is None:
        return 0
    else:

        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        # Use the larger one
        return max(lDepth, rDepth) + 1

"""
# we will use the level order traversal
This returns number of nodes
If want to use number of edges then we have to subtract 1 from height
Create a queue.
Push root into the queue.
height = 0
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
def maxDepthIterative(root):

    q = []
    q.append(root)
    height = 0
    while True:
        qsize = len(q)

        if qsize == 0:
            return height
        else:
            height += 1

        while qsize > 0:
            node = q.pop(0)

            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

            qsize -= 1










if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.add(15)
    tree.add(8)
    tree.add(18)
    tree.add(13)
    tree.add(7)
    tree.add(20)
    tree.add(22)
    print (maxDepth(tree.root))
    print(maxDepthIterative(tree.root))