from node import Node


class BinarySearchTree(object):

    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return self.root is None

    def get_root(self):
        return self.root

    def add(self, val):

        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):

        if node.value > val:

            if node.left is None:
                node.left = Node(val)
            else:
                self._add(val, node.left)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self._add(val, node.right)

    def size(self):
        pass

    def max_depth(self):
        pass

    def lookup(self, value):
        pass
        """
        static int lookup(struct node* node, int target) {
          // 1. Base case == empty tree
          // in that case, the target is not found so return false
          if (node == NULL) {
            return(false);
          }
          else {
            // 2. see if found here
            if (target == node->data) return(true);
            else {
              // 3. otherwise recur down the correct subtree
              if (target < node->data) return(lookup(node->left, target));
              else return(lookup(node->right, target));
            }
          }
        }

        """

    def print_inorder(self):
        
        """
        1) Create an empty stack S.
        2) Initialize current node as root
        3) Push the current node to S and set current = current->left until current is NULL
        4) If current is NULL and stack is not empty then 
            a) Pop the top item from stack.
            b) Print the popped item, set current = popped_item->right 
            c) Go to step 3.
        5) If current is NULL and stack is empty then we are done. 

        cur = self.root
        stack = []
        done = 0
        while not done:
            # Insert all the left values
            while cur is not None:
                #print (cur.value)
                stack.append(cur)
                cur = cur.left
            if cur is None and stack:
                popped = stack.pop()
                print(popped.value)
                cur = popped.right
            if cur is None and not stack:
                done = 1
        """
        cur = self.root
        stack = []
        done = 0
        while not done:

            # get all the left values
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            if cur is None and stack:
                # pop the last value:
                popped = stack.pop()
                print(popped.value)
                # check for right child
                cur = popped.right

            if cur is None and not stack:
                done = 1

    def DeleteTree(self):
        self.root = None

    # In order traversal using recursion
    def PrintTree(self):
        if self.root is not None:
            self._PrintTree(self.root)

    def _PrintTree(self, node):
        if node is not None:
            #print(str(node.value))
            self._PrintTree(node.left)
            print(str(node.value))
            self._PrintTree(node.right)
        else:
            print("In None")
            return

if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.add(15)
    tree.add(8)
    tree.add(18)
    tree.add(13)
    tree.add(7)
    tree.add(20)
    tree.add(22)
    tree.print_inorder()
    #tree.PrintTree()


class BinaryTree(object):

    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return self.root is None

    def add(self, val):

        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):

        if node.value > val:

            if node.left is None:
                node.left = Node(val)
            else:
                self._add(val, node.left)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self._add(val, node.right)

    def PrintTree(self):
        if self.root is not None:
            self._PrintTree(self.root)

    def _PrintTree(self, node):
        if node is not None:
            self._PrintTree(node.left)
            print(str(node.value))
            self._PrintTree(node.right)
        else:
            return

    def findMax(self):
        self._findMax(self.root)

    def _findMax(self, node):
            pass



"""
BFS vs DFS for Binary Tree
What are BFS and DFS for Binary Tree?
A Tree is typically traversed in two ways:

Breadth First Traversal (Or Level Order Traversal)
Depth First Traversals
Inorder Traversal (Left-Root-Right)
Preorder Traversal (Root-Left-Right)
Postorder Traversal (Left-Right-Root)

http://www.geeksforgeeks.org/bfs-vs-dfs-binary-tree/

"""




