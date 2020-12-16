# Course: CS261 - Data Structures
# Student Name: Casey Levy
# Assignment: Assignment 3 - queue_from_stacks.py
# Description: Creating methods for queue ADT using the stack ADT


from max_stack_sll import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new Queue based on two stacks
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.s1 = MaxStack()  # use as main storage
        self.s2 = MaxStack()  # use as temp storage

    def __str__(self) -> str:
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.s1.size()) + " elements. "
        out += str(self.s1)
        return out

    def is_empty(self) -> bool:
        """
        Return True if queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.s1.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.s1.size()

    # ------------------------------------------------------------------ #

    def enqueue(self, value: object) -> None:
        """
        Adds a new value to the end of the queue.
        """
        self.s1.push(value)
        return

    def dequeue(self) -> object:
        """
        Removes and returns the value from the beginning of the queue.
        If the queue is empty, raises QueueException.
        """
        if self.s1.is_empty():
            raise QueueException

        length = self.s1.size()
        for i in range(length):
            if i == length - 1:
                first_val = self.s1.pop()

            else:
                value = self.s1.pop()
                self.s2.push(value)

        for i in range(length - 1):
            self.s1.push(self.s2.pop())

        return first_val





# BASIC TESTING
if __name__ == "__main__":
    pass

    # print('\n# enqueue example 1')
    # q = Queue()
    # print(q)
    # for value in [1, 2, 3, 4, 5]:
    #     q.enqueue(value)
    # print(q)
    #
    # print('\n# dequeue example 1')
    # q = Queue()
    # for value in [1, 2, 3, 4, 5]:
    #     q.enqueue(value)
    # print(q)
    # for i in range(6):
    #     try:
    #         print(q.dequeue(), q)
    #     except Exception as e:
    #         print("No elements in queue", type(e))



