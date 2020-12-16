# Course: CS261 - Data Structures
# Student Name: 
# Assignment: Assignment 4 - bst.py
# Description: Creating various methods for binary search tree, inclduing traversal and
#                  operational functions.


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"




class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self) -> object:
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"




class TreeNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value          # to store node's data
        self.left = None            # pointer to root of left subtree
        self.right = None           # pointer to root of right subtree

    def __str__(self):
        return str(self.value)




class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE in order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does in-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if cur is None:
            return
        # recursive case for left subtree
        self._str_helper(cur.left, values)
        # store value of current node
        values.append(str(cur.value))
        # recursive case for right subtree
        self._str_helper(cur.right, values)



    def add(self, value: object) -> None:
        """
        Adds new value to the tree, maintaining BST property.
        """
        if self.root is None:         # If tree is empty
            self.root = TreeNode(value)
            return

        child_node = self.root
        parent_node = None
        while child_node is not None:      # Traversing the tree
            parent_node = child_node
            if value < child_node.value:
                child_node = child_node.left

            else:
                child_node = child_node.right

        if value < parent_node.value:
            parent_node.left = TreeNode(value)     # Add new node as child of parent

        else:
            parent_node.right = TreeNode(value)



    def contains(self, value: object) -> bool:
        """
        Returns True if value parameter is in the BST or False if it isn't.
        False is also returned if tree is empty.
        """
        cur = self.root
        while cur is not None:
            if value == cur.value:
                return True

            elif value < cur.value:
                cur = cur.left

            else:
                cur = cur.right

        return False



    def get_first(self) -> object:
        """
        Returns value stored in root node. If tree is empty, method should return None.
        """
        if self.root is None:        # If tree is empty
            return None

        return self.root.value       # Returning root value



    def remove(self, value) -> bool:
        """
        Removes the first instance of the object in the tree. Must return True
           if the value is removed, False if not
        """
        left_bool = False
        found = False           # Traversing the tree
        parent = None
        node_to_remove = self.root

        while node_to_remove is not None and not found:
            if value == node_to_remove.value:
                found = True

            elif value < node_to_remove.value:
                parent= node_to_remove
                node_to_remove = node_to_remove.left
                left_bool = True

            else:
                parent = node_to_remove
                node_to_remove = node_to_remove.right
                left_bool = False

        if not node_to_remove:     # If value is not found in tree
            return False

        if node_to_remove == self.root:     # If the node to remove is the root node
            self.remove_first()
            return True

        if self.leaf(node_to_remove) and left_bool:     # If node to remove is a leaf
            parent.left = None
            return  True

        if self.leaf(node_to_remove) and not left_bool:     # If node to remove only has left subtree
            parent.right = None
            return True

        if node_to_remove.right is None and left_bool:
            parent.left = node_to_remove.left
            return True

        if node_to_remove.right is None and not left_bool:
            parent.right = node_to_remove.left
            return True

        left_bool_2 = False           # Case if ndoe to remove has a right subtree
        replace = node_to_remove.right
        parent_replace = node_to_remove

        while replace.left is not None:
            parent_replace = replace
            replace = replace.left
            left_bool_2 = True

        if left_bool_2:
            parent_replace.left = replace.right
        if not left_bool_2:
            parent_replace.right = replace.right

        if left_bool:
            parent.left = replace
            replace.left = node_to_remove.left
            replace.right = node_to_remove.right
            return True
        if not left_bool:
            parent.right = replace
            replace.left = node_to_remove.left
            replace.right = node_to_remove.right
            return True


    def leaf(self, node: object) -> bool:
        """
         Helper function. Determines whether argument passed is a leaf
        """
        if node.left is None and node.right is None:
            return True

        else:
            return False



    def remove_first(self) -> bool:
        """
        Removes the root node in the tree. Method must return False if the tree is
           empty and there is no root node to be removed and True if it is removed
        """
        if self.root is None:     # If tree is empty
            return False

        if self.leaf(self.root):     # If root is a lead
            self.root = None
            return True

        if self.root.right is None:
            self.root = self.root.left    # Case where root has no right subtree
            return True

        replace = self.root.right          # Case where root has right subtree
        parent_replace = self.root
        left_bool = False

        while replace.left is not None:
            parent_replace = replace
            replace = replace.left
            left_bool = True

        if left_bool:
            parent_replace.left = replace.right

        else:
            parent_replace.right = replace.right

        replace.left = self.root.left     # Placing leftmost child into root spot
        replace.right = self.root.right
        self.root = replace
        return True


    def pre_order_helper(self, node: object, q: object) -> None:
        """
        Recursive helper function for pre-order traversal
        """
        q.enqueue(node)
        if node.left is not None:          # If node.left exists
            self.pre_order_helper(node.left, q)

        if node.right is not None:          # If node.right exists
            self.pre_order_helper(node.right, q)



    def pre_order_traversal(self) -> Queue:
        """
        Performs pre-order traversal of tree
        """
        q = Queue()      # Initializing queue
        if self.root is None:      # If tree is empty
            return q

        self.pre_order_helper(self.root, q)
        return q


    def in_order_helper(self, node: object, q: object) -> None:
        """
        recursive helper function for in-order traversal
        """
        if node.left is not None:        # If node.left exists
            self.in_order_helper(node.left, q)

        q.enqueue(node)               # Process current node

        if node.right is not None:            # If node.right exists
            self.in_order_helper(node.right, q)



    def in_order_traversal(self) -> Queue:
        """
        Performs in-order traversal on the tree
        """
        q = Queue()          # Initializing queue
        if self.root is None:        # If tree is empty
            return q

        self.in_order_helper(self.root, q)          # Using helper function if tree isn't empty and returning Queue
        return q



    def post_order_helper(self, node: object, q: object) -> None:
        """
        Recursive helper function for post-order traversal
        """
        if node.left is not None:            # If node.left exists
            self.post_order_helper(node.left, q)

        if node.right is not None:            # If node.right exists
            self.post_order_helper(node.right, q)

        q.enqueue(node)                 # Processing current node


    def post_order_traversal(self) -> Queue:
        """
        Performs post-order traversal on the tree
        """
        q = Queue()         # Initializing queue
        if self.root is None:       # If tree is empty
            return q

        self.post_order_helper(self.root, q)      # Using helper function if tree isn't empty and returning Queue
        return q


    def by_level_traversal(self) -> Queue:
        """
        performs by-level traversal on tree
        """
        q = Queue()           # Initializing queue
        final_q = Queue()
        if self.root is None:       # If tree is empty
            return final_q

        q.enqueue(self.root)          # Begin process, placing root node in working queue

        while not q.is_empty():        # Traversing tree, adding nodes to q
            node = q.dequeue()
            if node is not None:
                final_q.enqueue(node)
                q.enqueue(node.left)
                q.enqueue(node.right)

        return final_q


    def is_full_helper(self, node: object) -> bool:
        """
        Recursive helper function for is_full method
        """
        if self.leaf(node):         # Handling case if node is a leaf
            return True

        if node.left is None and node.right is not None:
            return False
                                                              # Case where node has a single child
        if node.left is not None and node.right is None:
            return False

        return True and self.is_full_helper(node.left) and self.is_full_helper(node.right)



    def is_full(self) -> bool:
        """
        Checks and indicates if tree is full
        """
        if self.root is None:      # If tree is empty
            return True

        if self.root.left is None and self.root.right is None:      # If tree has single root node
            return True

        return self.is_full_helper(self.root)



    def complete_helper(self, node, index, num_nodes) -> bool:
        """
        Recursive helper functions for is_complete method
        """
        if node is None:   # Establishing base case
            return True

        if index >= num_nodes:
            return False

        else:
            return (self.complete_helper(node.left, 2*index+1, num_nodes)) and (
                self.complete_helper(node.right, 2*index+2, num_nodes)
            )

    def is_complete(self) -> bool:
        """
        Determines and indicates if tree is complete
        """
        if self.root is None or self.root.left is None and self.root.right is None:
            return True       # Empty tree or has one node is considered complete

        else:                    # Creating base index to begin traversal
            index = 0
            count = self.size()
            return self.complete_helper(self.root, index, count

                                        )
    def is_perfect_helper(self, node: object, iterator: int, iterator_limit: int) -> bool:
        """
        Recursive helper function for is_perfect method
        """
        if iterator == iterator_limit:
            return True

        if node.left is None or node.right is None:     # Case if node with more than 2 children
            return False

        return self.is_perfect_helper(node.left, iterator+1, iterator_limit) and self.is_perfect_helper(node.right, iterator+1, iterator_limit)



    def is_perfect(self) -> bool:
        """
        Determines and indicates if tree is perfect
        """
        if self.root is None:      # If tree is empty
            return True

        h = self.height()
        return self.is_perfect_helper(self.root, 0, h)



    def size_helper(self, node: object) -> int:
        """
        Recursive helper function for size method
        """
        count = 1
        if node.left is not None:            # Calling helper on left subtree of current node
            count += self.size_helper(node.left)

        if node.right is not None:           # Calling helper on right subtree of current node
            count += self.size_helper(node.right)
        return count



    def size(self) -> int:
        """
        Returns number of tree nodes
        """
        if self.root is None:         # If tree is empty
            return 0

        return self.size_helper(self.root)


    def height_helper(self, node: object) -> int:
        """
        Recursive helper function for height method
        """
        if self.leaf(node):           # If current node is a leaf
            return 0

        if node.left is not None and node.right is None:
            return 1 + self.height_helper(node.left)

        if node.left is None and node.right is not None:
            return 1 + self.height_helper(node.right)

        # If node has two children
        if self.height_helper(node.left) > self.height_helper(node.right):
            return 1 + self.height_helper(node.left)

        else:
            return 1 + self.height_helper(node.right)



    def height(self) -> int:
        """
        Returns the height of the tree
        """
        if self.root is None:
            return -1

        return self.height_helper(self.root)



    def count_helper(self, node: object) -> int:
        """
        Recursive helper function for count_leaves method
        """
        if self.leaf(node):        # If current node is a leaf
            return 1

      # Cases if current node has a single child
        if node.left is not None and node.right is None:
            return self.count_helper(node.left)

        if node.left is None and node.right is not None:
            return self.count_helper(node.right)

        # Case where current node has two children
        return self.count_helper(node.left) + self.count_helper(node.right)



    def count_leaves(self) -> int:
        """
        Counts and returns number of leaves that have no children
        """
        if self.root is None:       # If tree is empty
            return 0

        return self.count_helper(self.root)



    def unique_helper(self, node: object, q: object) -> int:
        """
        Recursive helper function for count_unique method
        """
        temp = Queue()       # Initializing queue and then iterating through
        new_val = True

        while not q.is_empty() and new_val:
            current = q.dequeue()
            temp.enqueue(current)
            if node.value == current.value:
                new_val = False

        while not temp.is_empty():         # Enqueue nodes from temp into q
            current = temp.dequeue()
            q.enqueue(current)

        add_current = 0

        if new_val:
            q.enqueue(node)
            add_current = 1

        if self.leaf(node):        # If current node is a leaf
            return add_current

        # Cases where current node has a single child
        if node.left is not None and node.right is None:
            return add_current + self.unique_helper(node.left, q)

        if node.left is None and node.right is not None:
            return add_current + self.unique_helper(node.right, q)

        return add_current + self.unique_helper(node.left, q) + self.unique_helper(node.right, q)



    def count_unique(self) -> int:
        """
        Counts and returns number of nodes with unique values
        """
        if self.root is None:   # If tree is empty
            return 0

        q = Queue()
        return self.unique_helper(self.root, q)



# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':
    """ add() example #1 """
    print("\nPDF - method add() example 1")
    print("----------------------------")
    tree = BST()
    print(tree)
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree)
    tree.add(15)
    tree.add(15)
    print(tree)
    tree.add(5)
    print(tree)

    """ add() example 2 """
    print("\nPDF - method add() example 2")
    print("----------------------------")
    tree = BST()
    tree.add(10)
    tree.add(10)
    print(tree)
    tree.add(-1)
    print(tree)
    tree.add(5)
    print(tree)
    tree.add(-1)
    print(tree)

    """ contains() example 1 """
    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    """ contains() example 2 """
    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    """ get_first() example 1 """
    print("\nPDF - method get_first() example 1")
    print("----------------------------------")
    tree = BST()
    print(tree.get_first())
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree.get_first())
    print(tree)

    """ remove() example 1 """
    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    tree = BST([10, 5, 15])
    print(tree.remove(7))
    print(tree.remove(15))
    print(tree.remove(15))

    """ remove() example 2 """
    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.remove(20))
    print(tree)

    """ remove() example 3 """
    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
    print(tree.remove(20))
    print(tree)
    # comment out the following lines
    # if you have not yet implemented traversal methods
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ remove_first() example 1 """
    print("\nPDF - method remove_first() example 1")
    print("-------------------------------------")
    tree = BST([10, 15, 5])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 2 """
    print("\nPDF - method remove_first() example 2")
    print("-------------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 3 """
    print("\nPDF - method remove_first() example 3")
    print("-------------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)

    """ Traversal methods example 1 """
    print("\nPDF - traversal methods example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Traversal methods example 2 """
    print("\nPDF - traversal methods example 2")
    print("---------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 1 """
    print("\nComprehensive example 1")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'  N/A {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print()
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 2 """
    print("\nComprehensive example 2")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'N/A   {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in 'DATA STRUCTURES':
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print('', tree.pre_order_traversal(), tree.in_order_traversal(),
          tree.post_order_traversal(), tree.by_level_traversal(),
          sep='\n')

