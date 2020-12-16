# Course: CS261 - Data Structures
# Assignment: 5
# Student:
# Description: Creating various methods for min_heap


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0



    def add(self, node: object) -> None:
        """
        Adds a new object to the MinHeap maintaining heap property
        """
        self.heap.append(node)              # Appending node to end of DynArray
        if self.heap.length() == 1:         # Case if heap is empty
            return

        child_node = self.heap.length() - 1      # Swapping child node with parent node until it is greater
        parent_node = (child_node-1) // 2

        while self.heap.get_at_index(parent_node) > self.heap.get_at_index(child_node) and child_node != 0:
            self.heap.swap(parent_node, child_node)
            child_node = parent_node
            parent_node = (child_node-1) // 2



    def get_min(self) -> object:
        """
        Returns an object with a minimum key without removing it from the heap.
        MinHeapException is raised if heap is empty.
        Runtime must be O(1)
        """
        if self.heap.length() == 0:       # Case if heap is empty
            raise MinHeapException

        return self.heap.get_at_index(0)



    def remove_min(self) -> object:
        """
        Returns an object with a minimum key and removes it from the heap.
        MinHeapException is raised if heap is empty.
        Runtime must be O(logN)
        """
        if self.is_empty():             # Case if heap is empty
            raise MinHeapException

        min = self.heap.get_at_index(0)
        self.heap.swap(0, self.heap.length()-1)
        self.heap.pop()

        replacement = 0

        while True:
            if self.is_empty():
                break

            child1 = 2 * replacement + 1
            child2 = 2 * replacement + 2

            if child1 >= self.heap.length():
                break

            min_index = child1

            if child2 < self.heap.length():
                if self.heap.get_at_index(child2) < self.heap.get_at_index(child1):
                    min_index = child2

            if self.heap.get_at_index(replacement) > self.heap.get_at_index(min_index):
                self.heap.swap(replacement, min_index)
                replacement = min_index

            else:
                break

        return min



    def build_heap(self, da: DynamicArray) -> None:
        """
        Method receives a dynamic array with objects in any order and builds a proper
           MinHeap from them. Runtime complexity must be O(n).
        """
        self.heap = DynamicArray()      # Setting self.heap to empty array
        for i in range(da.length()):    # Copying each element to new self.heap
            self.heap.append(da.get_at_index(i))

        len = self.heap.length()
        if len == 1:
            return

        else:
            first_index = len // 2-1
            for i in range(first_index, -1, -1):   # Traversing over indices
                parent_ind = i
                parent_node = self.heap.get_at_index(parent_ind)

                while parent_ind < len:
                    left_ind = parent_ind * 2 + 1
                    right_ind = parent_ind * 2 + 2
                    left_node = None
                    right_node = None

                    if left_ind < len:
                        left_node = self.heap.get_at_index(left_ind)

                    if right_ind < len:
                        right_node = self.heap.get_at_index(right_ind)

                    # Setting various if/else statements based on node conditions

                    # Setting smaller child node to min_node
                    if left_node is not None and right_node is not None:
                        min_node = min(left_node, right_node)
                        if min_node == left_node:
                            min_ind = left_ind

                        else:
                            min_ind = right_ind

                    elif left_node is not None and right_node is None:
                        min_node = left_node
                        min_ind = left_ind

                    elif right_node is not None and not left_node is None:
                        min_node = right_node
                        min_ind = right_ind

                    else:
                        break


                    if parent_node > min_node:
                        self.heap.swap(parent_ind, min_ind)
                        parent_ind = min_ind
                        parent_node = self.heap.get_at_index(parent_ind)

                    else:
                        break



# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
