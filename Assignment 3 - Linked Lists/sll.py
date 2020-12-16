# Course: CS261 - Data Structures
# Student Name: Casey Levy
# Assignment: Assignment 3 - sll.py
# Description: Creating various methods for deque and bag ADT using singly linked list



class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.head.next == self.tail

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        Adds a new node to the beginning of the list (after front sentinel)
        """
        new_node = SLNode(value)

        new_node.next = self.head.next
        self.head.next = new_node
        return



    def add_back(self, value: object) -> None:
        """
        Adds new node to end of the list (before back sentinel)
        """
        # traverse the list to find last node

        new_node = SLNode(value)

        cur = self.head.next
        prev = self.head

        while cur != self.tail:
            prev = cur
            cur = cur.next

        prev.next = new_node
        new_node.next = self.tail
        return



    def insert_at_index(self, index: int, value: object) -> None:
        """
        Adds a new value at specified index location. If provided index is invalid, SLLException is raised
        """
        if index < 0 or index > self.length():   # If given index is invalid
            raise SLLException

        new_node = SLNode(value)
        if index == 0 and self.length() == 0:     # Setting given value as first value if list is essentially empty
            self.head.next = new_node
            new_node.next = self.tail
            return

        if index == 0:
            cur = self.head.next
            self.head.next = new_node
            new_node.next = cur
            return

        cur = self.head.next
        prev = None
        position = 0

        while position != index:
            prev = cur
            cur = cur.next
            position += 1

        prev.next = new_node
        new_node.next = cur



    def remove_front(self) -> None:
        """
        Removes first node from the list. If list is empty, SLLException is raised.
        """
        if self.head.next == self.tail:
            raise SLLException

        self.head.next = self.head.next.next
        return



    def remove_back(self) -> None:
        """
        Removes last node from list. If list is empty, SLLException is raised
        """
        if self.is_empty():
            raise SLLException

        prev = None
        cur = self.head

        while cur.next != self.tail:
            prev = cur
            cur = cur.next

        prev.next = self.tail
        return



    def remove_at_index(self, index: int) -> None:
        """
        Removes node at given index. If given index is invalid, SLLException is raised.
        """
        prev = self.head
        cur = self.head.next

        if index < 0 or cur == self.tail:
            raise SLLException

        for i in range(index):
            if cur.next == self.tail:
                raise SLLException

            prev = cur
            cur = cur.next

        prev.next = cur.next
        return



    def get_front(self) -> object:
        """
        Returns value from first node in list without removing. SLLException is raised if list is empty
        """
        if self.head.next == self.tail:
            raise SLLException

        return self.head.next.value



    def get_back(self) -> object:
        """
        Returns value from last node without removing. SLLException is raised if list is empty.
        """
        prev = self.head
        cur = self.head.next

        if cur == self.tail:
            raise SLLException

        while cur.next != self.tail:
            prev = cur
            cur = cur.next

        return cur.value



    def remove(self, value: object) -> bool:
        """
        Traverses the list from beginning to end and removes the first node in the list that matches
           the provided "value" object. Returns True if a node is removed, False if not.
        """
        cur = self.head

        while cur != self.tail:
            if cur.next.value == value:
                cur.next = cur.next.next
                return True

            else:
                cur = cur.next

        return False



    def count(self, value: object) -> int:
        """
        Counts number of elements in list that match provided "value" object
        """
        if self.is_empty():
            return 0

        prev = self.head
        cur = self.head.next
        val_count = 0

        while cur != self.tail:
            if cur.value == value:
                val_count += 1
            prev = cur
            cur = cur.next

        return val_count



    def slice(self, start_index: int, size: int) -> object:
        """
        Returns a new LinkedList object that contains requested number of nodes from original list, starting
           with the node located at requested start index. If original list contains N nodes, valid start_index is in range
           [0, N - 1] inclusive. Runtime must be O(n). SLLException is raised if provided start index is invalid, or if
           there are not enough nodes between start index and end of list to make the slice of requested size
        """
        x = self.length()

        if start_index < 0 or start_index >= x or size < 0 or (start_index + size) > x:
            raise SLLException

        new_list = LinkedList()
        node = self.head

        for i in range(start_index + 1):
            node = node.next

        for i in range(size):
            new_list.add_back(node.value)
            node = node.next

        return new_list





if __name__ == '__main__':
    pass

    # print('\n# add_front example 1')
    # list = LinkedList()
    # print(list)
    # list.add_front('A')
    # list.add_front('B')
    # list.add_front('C')
    # print(list)
    #
    #
    # print('\n# add_back example 1')
    # list = LinkedList()
    # print(list)
    # list.add_back('C')
    # list.add_back('B')
    # list.add_back('A')
    # print(list)
    #
    #
    # print('\n# insert_at_index example 1')
    # list = LinkedList()
    # test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    # for index, value in test_cases:
    #     print('Insert of', value, 'at', index, ': ', end='')
    #     try:
    #         list.insert_at_index(index, value)
    #         print(list)
    #     except Exception as e:
    #         print(type(e))
    #
    #
    # print('\n# remove_front example 1')
    # list = LinkedList([1, 2])
    # print(list)
    # for i in range(3):
    #     try:
    #         list.remove_front()
    #         print('Successful removal', list)
    #     except Exception as e:
    #         print(type(e))
    #
    #
    # print('\n# remove_back example 1')
    # list = LinkedList()
    # try:
    #     list.remove_back()
    # except Exception as e:
    #     print(type(e))
    # list.add_front('Z')
    # list.remove_back()
    # print(list)
    # list.add_front('Y')
    # list.add_back('Z')
    # list.add_front('X')
    # print(list)
    # list.remove_back()
    # print(list)
    #
    #
    # print('\n# remove_at_index example 1')
    # list = LinkedList([1, 2, 3, 4, 5, 6])
    # print(list)
    # for index in [0, 0, 0, 2, 2, -2]:
    #     print('Removed at index:', index, ': ', end='')
    #     try:
    #         list.remove_at_index(index)
    #         print(list)
    #     except Exception as e:
    #         print(type(e))
    # print(list)
    #
    #
    # print('\n# get_front example 1')
    # list = LinkedList(['A', 'B'])
    # print(list.get_front())
    # print(list.get_front())
    # list.remove_front()
    # print(list.get_front())
    # list.remove_back()
    # try:
    #     print(list.get_front())
    # except Exception as e:
    #     print(type(e))
    #
    #
    # print('\n# get_back example 1')
    # list = LinkedList([1, 2, 3])
    # list.add_back(4)
    # print(list.get_back())
    # list.remove_back()
    # print(list)
    # print(list.get_back())
    #
    #
    # print('\n# remove example 1')
    # list = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(list)
    # for value in [7, 3, 3, 3, 3]:
    #     print(list.remove(value), list.length(), list)
    #
    #
    # print('\n# count example 1')
    # list = LinkedList([1, 2, 3, 1, 2, 2])
    # print(list, list.count(1), list.count(2), list.count(3), list.count(4))
    #
    #
    # print('\n# slice example 1')
    # list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # ll_slice = list.slice(1, 3)
    # print(list, ll_slice, sep="\n")
    # ll_slice.remove_at_index(0)
    # print(list, ll_slice, sep="\n")
    #
    #
    # print('\n# slice example 2')
    # list = LinkedList([10, 11, 12, 13, 14, 15, 16])
    # print("SOURCE:", list)
    # slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    # for index, size in slices:
    #     print("Slice", index, "/", size, end="")
    #     try:
    #         print(" --- OK: ", list.slice(index, size))
    #     except:
    #         print(" --- exception occurred.")

